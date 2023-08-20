#!/bin/sh

export TZ=UTC
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
OUTPUT_ZIP=${PWD}/lambda_${TIMESTAMP}.zip

VENV=$(pipenv --venv)
pushd ${VENV}/lib/python3.7/site-packages
ls | grep -v boto | xargs zip -r9 ${OUTPUT_ZIP}
popd
find . -name "*.py" | xargs zip -r9 ${OUTPUT_ZIP}
