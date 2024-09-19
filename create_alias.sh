#!/bin/bash

SCRIPT_DIR=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
ALIAS_NAME=py-notify
MAIN_SCRIPT=$SCRIPT_DIR/main.py

# Create alias
echo "alias $ALIAS_NAME='python3 $MAIN_SCRIPT'" >> ~/.bashrc

# Source the updated bashrc and zshrc
source ~/.bashrc
