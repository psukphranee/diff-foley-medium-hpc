#!/bin/bash

python main_panya.py \
--base ./configs/ldm_training/panya_config.yaml \
--model audio_contrastive_pretrained \
--name lr_8e-4_warmup200_wds_vgg+audioset_cnn14_pretrained_clip_num3_shift_lb8_intra_loss_w1 \