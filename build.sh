#!/bin/sh

#pip install python-minifier # if failed install this
NAME_SCRIPT="getnotex"

rm -rf bin

mkdir -p bin

pyminify ./src/get_note.py --output ./bin/$NAME_SCRIPT
sudo chmod +x bin/$NAME_SCRIPT