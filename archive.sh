#!/usr/bin/env bash
# archive.sh
# Usage:
#   ./archive.sh <expense_file>         # move file into archives/YYYY/MM/ and log
#   ./archive.sh search YYYY-MM-DD      # print archived expenses_YYYY-MM-DD.txt if present

set -euo pipefail

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
ARCHIVES_DIR="$BASE_DIR/archives"
LOG_FILE="$BASE_DIR/archive_log.txt"

mkdir -p "$ARCHIVES_DIR"

timestamp() {
  date "+%Y-%m-%d %H:%M:%S"
}

if [ "${1-}" = "search" ]; then
  if [ -z "${2-}" ]; then
    echo "Usage: $0 search YYYY-MM-DD"
    exit 1
  fi
  date="$2"
  pattern="expenses_$date.txt"
  found=0
  while IFS= read -r -d '' file; do
    echo "---- $file ----"
    cat "$file"
    found=1
  done < <(find "$ARCHIVES_DIR" -type f -name "$pattern" -print0 2>/dev/null)
  if [ "$found" -eq 0 ]; then
    echo "No archived file found for date $date"
  fi
  exit 0
fi

if [ -z "${1-}" ]; then
  echo "Usage: $0 <expense_file>   OR   $0 search YYYY-MM-DD"
  exit 1
fi

src="$1"
if [ ! -f "$src" ]; then
  if [ -f "$BASE_DIR/$src" ]; then
    src="$BASE_DIR/$src"
  else
    echo "File not found: $src"
    exit 1
  fi
fi

fname=$(basename "$src")
if [[ "$fname" =~ ^expenses_([0-9]{4})-([0-9]{2})-([0-9]{2})\.txt$ ]]; then
  yr="${BASH_REMATCH[1]}"
  mo="${BASH_REMATCH[2]}"
else
  yr=$(date "+%Y")
  mo=$(date "+%m")
fi

dest_dir="$ARCHIVES_DIR/$yr/$mo"
mkdir -p "$dest_dir"
dest="$dest_dir/$fname"

if mv "$src" "$dest"; then
  echo "[$(timestamp)] Moved $src -> $dest" >> "$LOG_FILE"
  echo "Archived to $dest"
else
  echo "Failed to move file."
  exit 1
fi
```// filepath: c:\Users\luigi\Downloads\tracker.py\archive.sh
#!/usr/bin/env bash
# archive.sh
# Usage:
#   ./archive.sh <expense_file>         # move file into archives/YYYY/MM/ and log
#   ./archive.sh search YYYY-MM-DD      # print archived expenses_YYYY-MM-DD.txt if present

set -euo pipefail

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
ARCHIVES_DIR="$BASE_DIR/archives"
LOG_FILE="$BASE_DIR/archive_log.txt"

mkdir -p "$ARCHIVES_DIR"

timestamp() {
  date "+%Y-%m-%d %H:%M:%S"
}

if [ "${1-}" = "search" ]; then
  if [ -z "${2-}" ]; then
    echo "Usage: $0 search YYYY-MM-DD"
    exit 1
  fi
  date="$2"
  pattern="expenses_$date.txt"
  found=0
  while IFS= read -r -d '' file; do
    echo "---- $file ----"
    cat "$file"
    found=1
  done < <(find "$ARCHIVES_DIR" -type f -name "$pattern" -print0 2>/dev/null)
  if [ "$found" -eq 0 ]; then
    echo "No archived file found for date $date"
  fi
  exit 0
fi

if [ -z "${1-}" ]; then
  echo "Usage: $0 <expense_file>   OR   $0 search YYYY-MM-DD"
  exit 1
fi

src="$1"
if [ ! -f "$src" ]; then
  if [ -f "$BASE_DIR/$src" ]; then
    src="$BASE_DIR/$src"
  else
    echo "File not found: $src"
    exit 1
  fi
fi

fname=$(basename "$src")
if [[ "$fname" =~ ^expenses_([0-9]{4})-([0-9]{2})-([0-9]{2})\.txt$ ]]; then
  yr="${BASH_REMATCH[1]}"
  mo="${BASH_REMATCH[2]}"
else
  yr=$(date "+%Y")
  mo=$(date "+%m")
fi

dest_dir="$ARCHIVES_DIR/$yr/$mo"
mkdir -p "$dest_dir"
dest="$dest_dir/$fname"

if mv "$src" "$dest"; then
  echo "[$(timestamp)] Moved $src -> $dest" >> "$LOG_FILE"
  echo "Archived to $dest"
else
  echo "Failed