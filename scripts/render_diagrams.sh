#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
mapfile -d '' diagrams < <(find "$ROOT/docs" -name '*.puml' -print0 | sort -z)

if (( ${#diagrams[@]} == 0 )); then
  echo "No PlantUML diagrams found" >&2
  exit 1
fi

check_with_plantuml() {
  local diagram="$1"
  echo "Checking PlantUML: ${diagram#"$ROOT/"}"
  plantuml -verbose -checkonly "$diagram"
}

check_with_docker() {
  local diagram="$1"
  local relative="${diagram#"$ROOT/"}"
  echo "Checking PlantUML: $relative"
  docker run --rm \
    -v "$ROOT:/work" \
    -w /work \
    plantuml/plantuml:1.2026.4 \
    -verbose -checkonly "$relative"
}

if command -v plantuml >/dev/null 2>&1; then
  for diagram in "${diagrams[@]}"; do
    check_with_plantuml "$diagram"
  done
  exit 0
fi

if command -v docker >/dev/null 2>&1; then
  for diagram in "${diagrams[@]}"; do
    check_with_docker "$diagram"
  done
  exit 0
fi

echo "PlantUML or Docker is required" >&2
exit 1
