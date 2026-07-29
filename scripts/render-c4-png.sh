#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIAGRAM_DIR="${DIAGRAM_DIR:-$ROOT_DIR/docs/architecture/diagrams/c4}"

if ! command -v rsvg-convert >/dev/null 2>&1; then
  echo "rsvg-convert não encontrado. Instale o pacote librsvg2-bin." >&2
  exit 1
fi

shopt -s nullglob
svg_files=("$DIAGRAM_DIR"/*.svg)

if [ "${#svg_files[@]}" -eq 0 ]; then
  echo "Nenhum SVG encontrado em $DIAGRAM_DIR." >&2
  exit 1
fi

for svg in "${svg_files[@]}"; do
  png="${svg%.svg}.png"
  rsvg-convert --zoom=1.5 --output "$png" "$svg"
  echo "Gerado: ${png#$ROOT_DIR/}"
done

echo "Gerados ${#svg_files[@]} diagramas PNG a partir dos SVGs canônicos."
