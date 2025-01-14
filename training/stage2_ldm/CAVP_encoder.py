import torch
import torch.nn as nn

import os

from open_clip.factory import get_model_config, list_models
from adm.modules.stage2_decode.clip_video_spec import CLIP_Video_Spec_v2, CLIP_Video_Spec


# initialize stage 1 model
def init_first_from_ckpt(path):
    model = torch.load(path, map_location="cpu")
    # 12.1.24 Panya: Loaded model from checkpoint in decode_wrapper.py
    print("Panya: Loaded model from checkpoint in decode_wrapper.py")
    if "state_dict" in list(model.keys()):
        model = model["state_dict"]
    # Remove: module prefix
    new_model = {}
    for key in model.keys():
        new_key = key.replace("module.","")
        new_model[new_key] = model[key]

    missing, unexpected = model.load_state_dict(new_model, strict=False)
    print(f"Restored from {path} with {len(missing)} missing and {len(unexpected)} unexpected keys")
    if len(missing) > 0:
        print(f"Missing Keys: {missing}")
    if len(unexpected) > 0:
        print(f"Unexpected Keys: {unexpected}")
    
    return model

def main():

    # load stage 1 config
    first_stage_config = get_model_config("audio_contrastive_pretrained")

    first_stage_config['target'] = 'adm.modules.stage2_decode.clip_video_spec.CLIP_Video_Spec_v2'
    first_stage_config['params'] = {
        "video_encode": "Slowonly",
        "spec_encode": "cnn14_pool",
        "embed_dim": 512
    }

    # load stage 1 checkpoint
    first_stage_ckpt_path = "/Users/920753844/Diff-Foley/training/open_cavp_main/logs/2024_10_21-14_32_19-lr_8e-4_warmup200_wds_vgg+audioset_cnn14_pretrained_clip_num3_shift_lb8_intra_loss_w1/checkpoints/epoch_latest.pt"

    model = init_first_from_ckpt(first_stage_ckpt_path)

if __name__ == "__main__":
    main()