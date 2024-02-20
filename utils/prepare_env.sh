#!/bin/sh

prepare_python_env() {
  pushd "$(dirname "$0")/.."
  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
  popd
  echo "To activate the virtual environment, execute:"
  echo "source venv/bin/activate"
}

prepare_python_env
