#!/bin/bash

python main.py \
--base ./configs/ldm_training/diff_foley_train.yaml \
-t --name diff_foley_experiment  \
--gpus 1 \
--stage 2 \
--epoch 250 \
--scale_lr False \
--max_epochs 5