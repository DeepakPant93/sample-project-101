#! /usr/bin/env bash

# Install fish terminal
sudo apt update -y
sudo apt-get install fish -y
pip install dvc

# Repo Initialization
make init-repo
git config --global --add safe.directory /workspaces/sample-project-101

# Install Dependencies
make reset-env
