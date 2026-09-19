#!/usr/bin/env bash
# Nightly backup of the SICVEC database (consistent snapshot) and uploaded receipts. Keeps 14 days.
set -euo pipefail
DATA=/var/lib/sicvec; OUT=/var/backups/sicvec; STAMP="$(date +%Y%m%d-%H%M%S)"
umask 077
python3 - "$DATA/sicvec.sqlite" "$OUT/sicvec-$STAMP.sqlite" <<'PY'
import sqlite3, sys
src = sqlite3.connect(sys.argv[1]); dst = sqlite3.connect(sys.argv[2])
src.backup(dst); dst.close(); src.close()
PY
tar -czf "$OUT/uploads-$STAMP.tar.gz" -C "$DATA" uploads
find "$OUT" -type f -mtime +14 -delete
