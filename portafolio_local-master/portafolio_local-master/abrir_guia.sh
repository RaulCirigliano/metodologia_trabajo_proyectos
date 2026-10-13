#!/usr/bin/env bash
# Abre la guía interactiva en tu navegador web predeterminado
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
cd "$DIR"

if command -v xdg-open >/dev/null 2>&1; then
    xdg-open index.html
elif command -v google-chrome >/dev/null 2>&1; then
    google-chrome index.html
elif command -v firefox >/dev/null 2>&1; then
    firefox index.html
else
    echo "Abre manualmente el archivo index.html en tu navegador preferido."
fi
