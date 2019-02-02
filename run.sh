#!/bin/bash

# Creating directory for data
mkdir -p /floyd/home/data/cryptokitty

# Creating symlink so code can access dataset
ln -s /floyd/input/data /floyd/home/data/cryptokitty/

#! cp -R /floyd/input/cryptokitty-256 /floyd/home/data/cryptokitty-256

# Running job
python train.py configs/cryptokitty.yaml
