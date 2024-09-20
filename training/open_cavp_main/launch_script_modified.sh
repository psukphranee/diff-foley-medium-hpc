#!/bin/bash


CUDA_VISIBLE_DEVICES=0 torchrun --nproc_per_node=1 -m src.training.main_wds_intra_contrast \
--batch-size 2 \
--data_dir '/Users/920753844/Diff-Foley/video' \
--dataset-type vggsound_audioset_music_webdataset_intra_contrast \
--epochs 1 \
--intra_clip_num 3 \
--intra_contrast_weight 1 \
--loss_type clip_intra_contrast \
--lr 8e-4 \
--model audio_contrastive_pretrained \
--name lr_8e-4_warmup200_wds_vgg+audioset_cnn14_pretrained_clip_num3_shift_lb8_intra_loss_w1 \
--precision amp \
--save-frequency 1 \
--save-most-recent \
--shift_lb 8 \
--spec_encode cnn14_pool \
--subset_num 400 \
--temporal_mix_weight 1 \
--train-data audioset_vggsound_music \
--train-num-samples 500 \
--val-frequency 2 \
--video_encode Slowonly_pool \
--warmup 100 \
--workers 1
