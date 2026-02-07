#!/bin/bash
# This starts the static web server

python3 src/main.py
cd public && python3 -m http.server 8888
