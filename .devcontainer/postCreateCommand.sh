#! /usr/bin/env bash

# Install fish terminal
sudo apt update -y
sudo apt-get install fish -y
pip install dvc

# Repo Initialization
make init-repo

# Install Dependencies
make reset-env
