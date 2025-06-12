#!/usr/bin/env bash

LED_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd $LED_DIR

rm -rf $LED_DIR/.venv
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
