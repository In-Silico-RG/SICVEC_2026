#!/usr/bin/env bash
# SICVEC 2026 — deploy (or update) the management app on a plain Debian/Ubuntu VPS.
#
# Usage (as root, on the VPS, from a copy of the repo's app/ directory):
#   sudo ./deploy/deploy.sh --domain sicvec.example.org --email you@unisucre.edu.co
#
# Needs: DNS A record for the domain already pointing to this VPS, ports 80 and 443 reachable.
# Idempotent: run it again to ship new code. It never overwrites /etc/sicvec/sicvec.env
# or the data in /var/lib/sicvec.
set -euo pipefail

DOMAIN=""; EMAIL=""
while [ $# -gt 0 ]; do
  case "$1" in
    --domain) DOMAIN="${2:-}"; shift 2 ;;
    --email)  EMAIL="${2:-}";  shift 2 ;;
    *) echo "Unknown argument: $1" >&2; exit 2 ;;
  esac
done
[ -n "$DOMAIN" ] && [ -n "$EMAIL" ] || { echo "Usage: $0 --domain <fqdn> --email <letsencrypt-email>" >&2; exit 2; }
[ "$(id -u)" -eq 0 ] || { echo "Run as root (sudo)." >&2; exit 1; }
command -v apt-get >/dev/null || { echo "Debian/Ubuntu only (needs apt-get)." >&2; exit 1; }

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"     # the app/ directory
[ -f "$SRC/run.py" ] || { echo "Cannot find run.py in $SRC; run from the repo's app/ directory." >&2; exit 1; }
APP=/opt/sicvec/app; VENV=/opt/sicvec/venv
ENVF=/etc/sicvec/sicvec.env; DATA=/var/lib/sicvec; BACKUPS=/var/backups/sicvec

echo "==> Packages"
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq python3 python3-venv rsync nginx certbot ufw curl >/dev/null

echo "==> User and directories"
id sicvec >/dev/null 2>&1 || useradd --system --home /opt/sicvec --shell /usr/sbin/nologin sicvec
install -d -o root -m 755 /opt/sicvec "$APP"
install -d -o sicvec -g sicvec -m 750 "$DATA" "$DATA/uploads"
install -d -o root -m 700 /etc/sicvec "$BACKUPS"
install -d -m 755 /var/www/certbot

echo "==> Code and virtualenv"
rsync -a --delete --exclude '.venv' --exclude 'instance' --exclude '.pytest_cache' \
      --exclude '__pycache__' --exclude 'tests' "$SRC/" "$APP/"
[ -d "$VENV" ] || python3 -m venv "$VENV"
"$VENV/bin/pip" install -q --upgrade pip
"$VENV/bin/pip" install -q "Flask>=3.0,<4" gunicorn        # runtime only, no pytest

echo "==> Environment file"
if [ ! -f "$ENVF" ]; then
  ADMIN_PW="$(python3 -c 'import secrets;print(secrets.token_urlsafe(18))')"
  umask 077
  cat > "$ENVF" <<ENV
SECRET_KEY=$(python3 -c 'import secrets;print(secrets.token_hex(32))')
ADMIN_PASSWORD=$ADMIN_PW
BASE_URL=https://$DOMAIN
SESSION_COOKIE_SECURE=1
DATABASE=$DATA/sicvec.sqlite
UPLOAD_DIR=$DATA/uploads
ONLINE_SEATS=300
# --- Fill these in, then: systemctl restart sicvec ---
# SMTP_HOST=
# SMTP_PORT=587
# SMTP_USER=
# SMTP_PASSWORD=
# MAIL_FROM=insilico@unisucre.edu.co
# CONSENT_TEXT=Texto oficial de tratamiento de datos de UNISUCRE
ENV
  echo
  echo "  Admin login (shown once, also stored in $ENVF):"
  echo "    user: admin    password: $ADMIN_PW"
  echo
else
  echo "  $ENVF exists, left untouched."
fi
chmod 600 "$ENVF"; chown root:root "$ENVF"

echo "==> systemd service"
install -m 644 "$SRC/deploy/sicvec.service" /etc/systemd/system/sicvec.service
systemctl daemon-reload
systemctl enable sicvec >/dev/null
systemctl restart sicvec

echo "==> nginx + TLS"
rm -f /etc/nginx/sites-enabled/default
# Stage 1: HTTP only, just for the certificate challenge. The app is NOT served over HTTP.
cat > /etc/nginx/sites-available/sicvec <<NGX
server {
    listen 80;
    server_name $DOMAIN;
    location /.well-known/acme-challenge/ { root /var/www/certbot; }
    location / { return 404; }
}
NGX
ln -sf /etc/nginx/sites-available/sicvec /etc/nginx/sites-enabled/sicvec
nginx -t && systemctl reload nginx
if [ ! -d "/etc/letsencrypt/live/$DOMAIN" ]; then
  certbot certonly --webroot -w /var/www/certbot -d "$DOMAIN" \
          --non-interactive --agree-tos -m "$EMAIL" \
    || { echo "Certificate request failed. Check that DNS for $DOMAIN points here and port 80 is open, then re-run." >&2; exit 1; }
fi
# Stage 2: full config from the template.
sed "s/__DOMAIN__/$DOMAIN/g" "$SRC/deploy/nginx-sicvec.conf" > /etc/nginx/sites-available/sicvec
install -m 644 "$SRC/deploy/nginx-ratelimit.conf" /etc/nginx/conf.d/sicvec-ratelimit.conf
install -m 644 "$SRC/deploy/nginx-proxy.conf" /etc/nginx/sicvec-proxy.conf
nginx -t && systemctl reload nginx
# certbot's systemd timer renews; reload nginx after each renewal.
install -d /etc/letsencrypt/renewal-hooks/deploy
printf '#!/bin/sh\nsystemctl reload nginx\n' > /etc/letsencrypt/renewal-hooks/deploy/reload-nginx
chmod +x /etc/letsencrypt/renewal-hooks/deploy/reload-nginx

echo "==> Firewall"
ufw allow OpenSSH >/dev/null; ufw allow 'Nginx Full' >/dev/null
ufw --force enable >/dev/null

echo "==> Nightly backup"
install -m 755 "$SRC/deploy/backup.sh" /usr/local/sbin/sicvec-backup
echo '30 2 * * * root /usr/local/sbin/sicvec-backup' > /etc/cron.d/sicvec-backup
chmod 644 /etc/cron.d/sicvec-backup

echo "==> Check"
sleep 2
systemctl is-active --quiet sicvec && echo "  service: active" || { echo "  service NOT active: journalctl -u sicvec -n 50" >&2; exit 1; }
CODE="$(curl -s -o /dev/null -w '%{http_code}' "https://$DOMAIN/" || true)"
echo "  https://$DOMAIN/ -> HTTP $CODE"
echo
echo "Done. Next: set SMTP and CONSENT_TEXT in $ENVF, then 'systemctl restart sicvec'."
