#!/bin/bash

set -e

VENV_NAME=${VENV_DIR:=venv}

if ! [ -e "${GITHUB_WORKSPACE}/${VENV_NAME}" ]; then
    python -m venv "${GITHUB_WORKSPACE}/${VENV_NAME}"
fi

source "${GITHUB_WORKSPACE}/${VENV_NAME}/bin/activate"

sh -c "pip install -r requirements.txt"

sh -c "python main.py"
