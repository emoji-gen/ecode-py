#!/bin/bash

set -eux -o pipefail

rm -rf dist/

poetry install
poetry build -f wheel
poetry run pytest
poetry run twine upload --repository pypi dist/*
