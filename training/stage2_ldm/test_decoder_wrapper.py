# import the module
import torch
import numpy as np

from adm.modules.stage2_decode.decode_wrapper import Decoder_Wrapper
from open_clip.factory import get_model_config, list_models

from adm.modules.stage2_decode.clip_video_spec import CLIP_Video_Spec_v2, CLIP_Video_Spec

import json

def main():
    
    # Assert that the function is callable
    assert callable(get_model_config), "get_model_config is not callable"
    print("Import sucessful: get_model_config() is callable.")

    # List available model
    print("Listing Available Models: -------------------------------------")
    models_avail = list_models()
    for model in models_avail:
        print(model)
    print("---------------------------------------------------------------")

    first_stage_config = get_model_config("audio_contrastive_pretrained")
    first_stage_config['target'] = 'adm.modules.stage2_decode.clip_video_spec.CLIP_Video_Spec_v2'
    first_stage_config['params'] = {
        "video_encode": "Slowonly",
        "spec_encode": "cnn14_pool",
        "embed_dim": 512
    }

    first_stage_ckpt_path = "/Users/920753844/Diff-Foley/training/open_cavp_main/logs/2024_10_21-14_32_19-lr_8e-4_warmup200_wds_vgg+audioset_cnn14_pretrained_clip_num3_shift_lb8_intra_loss_w1/checkpoints/epoch_latest.pt"

    # Debug
    print("Assert that CLIP_Video_Spec_v2 is importable.", CLIP_Video_Spec_v2)
    print("Assert that CLIP_Video_Spec is importable.", CLIP_Video_Spec)

    # Pretty-printing the JSON
    print("Loading configuration of audio_contrastive_pretrained: ----")
    pretty_json = json.dumps(first_stage_config, indent=4, sort_keys=True)
    print(pretty_json)
    print("---------------------------------------------------------------")

    # Create an instance of Decoder_Wrapper
    decoder_wrapper = Decoder_Wrapper(
        first_stage_config = first_stage_config,
        decoder_config=first_stage_config,
        scheduler_config=first_stage_config,
        monitor=None,
        first_stage_ckpt=first_stage_ckpt_path
    )

    # load one input video
    sample_video_path = "/Users/920753844/Diff-Foley/video/goodarchive_1/YwZOeyAQC8.video.jpg"
    sample_video_np = np.load(sample_video_path)
    sample_video_tensor = torch.tensor(sample_video_np)

    # 12/2/24 Panya
    print(sample_video_tensor.shape)

    # sample_video_out = decoder_wrapper.encode_first_stage_video_intra(sample_video_tensor)

    

if __name__ == "__main__":
    main()