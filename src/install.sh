#!/bin/bash

echo "McFoo Delivery App Installation Script"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py