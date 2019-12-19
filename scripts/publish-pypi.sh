#!/bin/bash

set -eu

if [ -n "${VIRTUAL_ENV:-}" ]; then
  printf "[ERROR] Please deactivate virtualenv before run the script.\n" 1>&2
  exit 1
fi

set -x

rm -rf venv-publish
python3 -m venv venv-publish
. venv-publish/bin/activate

pip install -r requirements-dev.txt
pip install wheel

rm -rf ecode.egg-info/
rm -rf dist/
rm -rf build/

python3 setup.py bdist_wheel
twine upload --repository pypi dist/*

rm -rf venv-publish
