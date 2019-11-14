#!/bin/sh

sudo apt update
sudo apt install -y python3-dev python3-venv build-essential postgresql postgresql-server-dev-all uwsgi uwsgi-plugin-python3 nginx
