#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

sudo python "${SCRIPT_DIR}/../src/install-analyzer-applet.py"