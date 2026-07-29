#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CACHE_DIR="${CACHE_DIR:-$ROOT/.cache/plantuml}"
PLANTUML_VERSION="${PLANTUML_VERSION:-1.2026.6}"
PLANTUML_JAR="${PLANTUML_JAR:-$CACHE_DIR/plantuml-$PLANTUML_VERSION.jar}"
PLANTUML_URL="https://github.com/plantuml/plantuml/releases/download/v${PLANTUML_VERSION}/plantuml-${PLANTUML_VERSION}.jar"
PLANTUML_SHA256="89948f14c93756c7a3fb7b69078ff37e8489fd79dd430c582b931e2f65358690"

mapfile -d '' diagrams < <(find "$ROOT/docs" -name '*.puml' -print0 | sort -z)

if (( ${#diagrams[@]} == 0 )); then
  echo "No PlantUML diagrams found" >&2
  exit 1
fi

for command in java curl sha256sum dot; do
  if ! command -v "$command" >/dev/null 2>&1; then
    echo "Required command not found: $command" >&2
    exit 1
  fi
done

mkdir -p "$CACHE_DIR"

if [ ! -f "$PLANTUML_JAR" ]; then
  echo "Downloading PlantUML ${PLANTUML_VERSION}..."
  curl --fail --location --silent --show-error \
    --retry 4 --retry-delay 2 --retry-all-errors \
    --output "$PLANTUML_JAR" \
    "$PLANTUML_URL"
fi

echo "${PLANTUML_SHA256}  ${PLANTUML_JAR}" | sha256sum --check --status || {
  echo "Invalid checksum for ${PLANTUML_JAR}." >&2
  rm -f "$PLANTUML_JAR"
  exit 1
}

for diagram in "${diagrams[@]}"; do
  echo "Checking PlantUML syntax: ${diagram#"$ROOT/"}"
  if ! java -DPLANTUML_LIMIT_SIZE=16384 -jar "$PLANTUML_JAR" --check-syntax "$diagram"; then
    echo "PlantUML parser diagnostic for ${diagram#"$ROOT/"}:" >&2
    java -DPLANTUML_LIMIT_SIZE=16384 -jar "$PLANTUML_JAR" -syntax < "$diagram" || true
    exit 1
  fi
done
