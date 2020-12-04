#!/usr/bin/env bash
base_dir=$(dirname "$0")
repo="$base_dir/.."
env="$base_dir/$1"

### file structure
# $repo
#  |-- $base_dir (_build):
#  |      |-- $env:
#  |            |-- app --> $apphome
#  |            |-- data --> $apphome/data
#  |-- app: source code --> $apphome
#  |-- data: the data --> $apphome/data
#  |-- base: docker base images

# $apphome
#  |-- venv: venv
#  |-- data: the data

### Environment
if [ $# != 1 ]; then
    echo "!> Missing environment information." 
    echo "!> Usage: $0 <lab | stg | pro>"
    exit
fi

### environment variable
# $apphome
if [ ! $apphome ]; then
  echo '!> Missing $apphome.' 
  echo "!> Run 'source $env/env.sh'"
  exit
fi

### create folder structure
if [[ ! -d $apphome ]]; then
  echo "mkdir -p $apphome"
        mkdir -p $apphome
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

if [ -d "$env/app" ]; then
  echo "cp -a $env/app/. $apphome/"
        cp -a $env/app/. $apphome/
fi

### update data folder
echo "cp -a $repo/data/. $apphome/data/"
      cp -a $repo/data/. $apphome/data/

if [ -d "$env/data" ]; then
  echo "cp -a $env/data/. $apphome/data/"
        cp -a $env/data/. $apphome/data/
fi

### run script
echo "-- Run the following script ----"
echo "cd $apphome/"
echo "source $apphome/venv/bin/activate"
