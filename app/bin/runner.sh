#!/bin/bash

echo "This is a tool to use for League of Legends statistics"

read -p "Enter a summoner name for statistics: " summoner

python3 ../src/runner_dataCollect.py "$summoner"

