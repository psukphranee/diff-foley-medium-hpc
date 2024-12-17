import glob
import logging
import os
import re
import subprocess
import sys
import random
import webdataset as wds
from datetime import datetime

import numpy as np
import torch
from torch import optim
from torch.cuda.amp import GradScaler



import sys
sys.path.append("../src")

from open_clip import create_model_and_transforms, trace_model, get_tokenizer, create_loss, create_model_and_transforms_video_spec
from training.data import get_data, tarfile_to_samples_nothrow
from training.distributed import is_master, init_distributed_device, broadcast_object
from training.logger import setup_logging
from training.params import parse_args
from training.scheduler import cosine_lr, const_lr, const_lr_cooldown
from training.train_wds_intra_contrast import train_one_epoch, evaluate
from training.file_utils import pt_load, check_exists, start_sync_process, remote_sync


LATEST_CHECKPOINT_NAME = "epoch_latest.pt"


def random_seed(seed=42, rank=0):
    torch.manual_seed(seed + rank)
    np.random.seed(seed + rank)
    random.seed(seed + rank)


def natural_key(string_):
    """See http://www.codinghorror.com/blog/archives/001018.html"""
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_.lower())]


def get_latest_checkpoint(path: str, remote : bool):
    # as writen, this glob recurses, so can pick up checkpoints across multiple sub-folders
    if remote:
        result = subprocess.run(["aws", "s3", "ls", path + "/"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result)
        if result.returncode == 1:
            return None
        checkpoints = [os.path.join(path, x.split(' ')[-1]) for x in result.stdout.decode().split('\n')[:-1]]
    else:
        checkpoints = glob.glob(path + '**/*.pt', recursive=True)
    if checkpoints:
        checkpoints = sorted(checkpoints, key=natural_key)
        return checkpoints[-1]
    return None


def main(args):

    print("DEBUG: Entering main() of load_CLIP_directly.py")
    args = parse_args(args)

    args.model = "audio_contrastive_pretrained"
    start_epoch = 1
    args.val_data = "audioset_vggsound_music"
    args.dataset_type = "vggsound_audioset_music_webdataset_intra_contrast"
    args.workers = 1
    args.data_dir = "/Users/920753844/Diff-Foley/video/goodarchive_1.tar"
    args.batch_size = 1

    
    data = get_data(args, (None, None), epoch=start_epoch, tokenizer=get_tokenizer(args.model))
    assert len(data), 'At least one train or eval dataset must be specified.'

    dataloader = data['val'].dataloader

    shard_list = wds.SimpleShardList([args.data_dir])

    samples = tarfile_to_samples_nothrow(shard_list)
    for i in samples:
        print(i)

    
if __name__ == "__main__":
    main(sys.argv[1:])
