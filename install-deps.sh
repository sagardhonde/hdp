#!/bin/bash

set -euo pipefail

# Disable Prompt for manual feedback
export DEBIAN_FRONTEND=noninteractive

pip3 install --no-cache-dir poetry
poetry config virtualenvs.create false
poetry install --no-dev --no-interaction --no-ansi
echo yes | poetry cache clear --all pypi