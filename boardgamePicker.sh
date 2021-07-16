#!/bin/bash
if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: 
    This program requires Python to run, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
  exit 1
else
    python3 ./boardgamePicker.py $1
fi