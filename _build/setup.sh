#!/usr/bin/env bash
base_dir=$(dirname "$0")
repo="$base_dir/.."
env="$base_dir/$1"

### environment variable
# $apphome

### file structure
# $repo
#  |-- $1: environment repo --> repo
#  |-- app: source code --> $apphome
#  |-- base: docker base image

# $apphome
#  |-- venv: venv

### create folder structure
if [[ ! -d $apphome ]]; then
  echo "mkdir $apphome"
        mkdir $apphome
fi

### set up virtual environment
if ! [ -d "$apphome/venv" ]; then
  echo "python3 -m venv $apphome/venv"
        python3 -m venv $apphome/venv
  echo "source $apphome/venv/bin/activate"
        source $apphome/venv/bin/activate
  echo "pip install -r $repo/base/requirements.txt"
        pip install -r $repo/base/requirements.txt
  echo "deactivate"
        deactivate
fi

### update latest source code
echo "cp -a $repo/app/. $apphome/"
      cp -a $repo/app/. $apphome/

echo "cp -a $env/app/. $apphome/"
      cp -a $env/app/. $apphome/

### run script
echo "source $apphome/venv/bin/activate"
