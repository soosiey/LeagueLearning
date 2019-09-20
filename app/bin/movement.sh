#!/bin/bash

echo "This is a tool to use for League of Legends statistics"

read -p "Enter a json file to use in the helper/summoners/ folder: " fname

python3 ../src/runner_dataMove.py "$fname"

