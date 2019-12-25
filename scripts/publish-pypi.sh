#!/bin/bash

set -eux -o pipefail

rm -rf dist/

poetry install
poetry build -f wheel
poetry run twine upload --repository testpypi dist/*
