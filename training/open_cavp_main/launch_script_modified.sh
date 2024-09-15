#!/bin/bash


CUDA_VISIBLE_DEVICES=0 torchrun --nproc_per_node=1 -m src.training.main_wds_intra_contrast \
--train-data audioset_vggsound_music --val-data 'Test/vggsound-{000001..000002}.tar' --train-num-samples 32 \
--batch-size 1 --precision amp --workers 1 --dataset-type vggsound_audioset_music_webdataset_intra_contrast \
--model audio_contrastive_pretrained \
--name lr_8e-4_warmup200_wds_vgg+audioset_cnn14_pretrained_clip_num3_shift_lb8_intra_loss_w1 --lr 8e-4 \
--subset_num 20000 --epochs 1 --warmup 200 --loss_type clip_intra_contrast --temporal_mix_weight 1 \
--save-frequency 1 --spec_encode cnn14_pool --video_encode Slowonly_pool --val-frequency 2 --save-most-recent \
--intra_clip_num 3 --shift_lb 8 --save-most-recent --intra_contrast_weight 1
