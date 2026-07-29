#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_DIR="${SOURCE_DIR:-$ROOT_DIR/docs/architecture/diagrams/c4/src}"
OUTPUT_DIR="${OUTPUT_DIR:-$ROOT_DIR/docs/architecture/diagrams/c4}"
CACHE_DIR="${CACHE_DIR:-$ROOT_DIR/.cache/plantuml}"

PLANTUML_VERSION="${PLANTUML_VERSION:-1.2026.6}"
PLANTUML_JAR="${PLANTUML_JAR:-$CACHE_DIR/plantuml-$PLANTUML_VERSION.jar}"
PLANTUML_URL="https://github.com/plantuml/plantuml/releases/download/v${PLANTUML_VERSION}/plantuml-${PLANTUML_VERSION}.jar"
PLANTUML_SHA256="89948f14c93756c7a3fb7b69078ff37e8489fd79dd430c582b931e2f65358690"

require_command() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Comando obrigatório não encontrado: $1" >&2
    exit 1
  fi
}

require_command java
require_command curl
require_command sha256sum
require_command dot

mkdir -p "$CACHE_DIR" "$OUTPUT_DIR"

if [ ! -f "$PLANTUML_JAR" ]; then
  echo "Baixando PlantUML ${PLANTUML_VERSION}..."
  curl --fail --location --silent --show-error \
    --output "$PLANTUML_JAR" \
    "$PLANTUML_URL"
fi

echo "${PLANTUML_SHA256}  ${PLANTUML_JAR}" | sha256sum --check --status || {
  echo "Checksum inválido para ${PLANTUML_JAR}." >&2
  rm -f "$PLANTUML_JAR"
  exit 1
}

shopt -s nullglob
sources=("$SOURCE_DIR"/*.puml)

if [ "${#sources[@]}" -eq 0 ]; then
  echo "Nenhum arquivo .puml encontrado em ${SOURCE_DIR}." >&2
  exit 1
fi

for source in "${sources[@]}"; do
  name="$(basename "${source%.puml}")"
  svg="$OUTPUT_DIR/$name.svg"
  png="$OUTPUT_DIR/$name.png"

  java -DPLANTUML_LIMIT_SIZE=16384 -jar "$PLANTUML_JAR" --svg -pipe < "$source" > "$svg"
  java -DPLANTUML_LIMIT_SIZE=16384 -jar "$PLANTUML_JAR" -pipe < "$source" > "$png"

  if ! grep -q '<svg' "$svg"; then
    echo "SVG inválido gerado para ${source}." >&2
    exit 1
  fi

  if [ ! -s "$png" ]; then
    echo "PNG vazio gerado para ${source}." >&2
    exit 1
  fi

  echo "Gerados: ${svg#$ROOT_DIR/} e ${png#$ROOT_DIR/}"
done

echo "Gerados ${#sources[@]} diagramas C4 em SVG e PNG a partir dos arquivos PlantUML."
