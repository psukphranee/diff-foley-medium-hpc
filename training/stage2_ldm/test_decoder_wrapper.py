# import the module
import torch
import numpy as np
import argparse
import os

from adm.modules.stage2_decode.decode_wrapper import Decoder_Wrapper
from open_clip.factory import get_model_config, list_models

from adm.modules.stage2_decode.clip_video_spec import CLIP_Video_Spec_v2, CLIP_Video_Spec

import json

def main(args):
    
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

    # -------------- Load video _----------------------------
    # This section tests the video enconding part of the decoder wrapper class (which inits CLIPV2 -----------------------------)
    # load one input video
    # sample_video_path = "/Users/920753844/Diff-Foley/video/goodarchive_1/YwZOeyAQC8.video.jpg"

    # Specify input video in cmd line arg
    # 12.18.24 Add dimension and permute tensor to match argument requirements. We may have to adjust this
    sample_video_path = args.input_video_file
    sample_video_np = np.load(sample_video_path)
    print("Numpy tensor shape (video):", sample_video_np.shape)

    sample_video_tensor = torch.tensor(sample_video_np).to(torch.float32).unsqueeze(0)
    print("PyTorch tensor shape before (video):", sample_video_tensor.shape)
    sample_video_tensor = sample_video_tensor.permute(0,1,4,2,3)
    print("PyTorch tensor shape after (video):", sample_video_tensor.shape)
    
    
    # -------------- Generate dummy audio -----------------------------------
    spec_dummy = torch.zeros(1, 128, 256)

    # -----------------------------------------------------------------------

    # -------------------- call forward directly

    output_dict = decoder_wrapper.model.forward(sample_video_tensor, spec_dummy)
    print("Panya: output_dict keys: ", output_dict.keys())


    # ----------------Save output -----------------------------------------
    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    if args.output_file:
        # Ensure output_file is saved in the script's directory
        output_file = os.path.join(script_directory, os.path.basename(args.output_file))
    else:
        # Get the base name of the input file (strip the path)
        input_video_file_basename = os.path.basename(args.input_video_file)
        # Replace extension and save in the script's directory
        output_file = os.path.join(
            script_directory,
            input_video_file_basename.rsplit('.', -1)[0] + ".npz"
        )

    # Save the file in the determined output path
    print("Saving to: ", output_file)
    # Save each key-value pair in the dictionary as a separate entry in the .npz file
    np.savez(output_file, **{key: value.detach().numpy() for key, value in output_dict.items()})

    
    
    
    # ---------------------------------------------------------------------------------------------------------------------------
    
    '''
    # This section tests the AUDIO enconding part of the decoder wrapper class (which inits CLIPV2 -----------------------------)
    # load one input spec
    sample_audio_path = args.input_audio_file
    sample_audio_np = np.load(sample_audio_path)
    print("Numpy tensor shape (audio):", sample_audio_np.shape)

    # sample_audio_tensor = torch.tensor(sample_audio_np).to(torch.float32).unsqueeze(0)
    # print("PyTorch tensor shape before:", sample_audio_tensor.shape)
    # sample_audio_tensor = sample_audio_tensor.permute(0,1,4,2,3)
    # print("PyTorch tensor shape after:", sample_audio_tensor.shape)

    # sample_audio_out = decoder_wrapper.encode_first_stage_audio_intra(sample_audio_tensor)
    
    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    if args.output_file:
        # Ensure output_file is saved in the script's directory
        output_file = os.path.join(script_directory, os.path.basename(args.output_file))
    else:
        # Get the base name of the input file (strip the path)
        input_audio_file_basename = os.path.basename(args.input_audio_file)
        # Replace extension and save in the script's directory
        output_file = os.path.join(
            script_directory,
            input_audio_file_basename.rsplit('.', 0)[0] + ".npz"
        )
    '''
    # Save the file in the determined output path
    print("Saving to: ", output_file)
    np.savez(output_file)
    # ---------------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    # Create the argument parser
    parser = argparse.ArgumentParser(description="A script that demonstrates command-line arguments.")

    # Define the command-line arguments
    parser.add_argument("--input_video_file", type=str, required=False, help="Path to the input video file.")
    parser.add_argument("--input_audio_file", type=str, required=False, help="Path to the input audio file.")
    parser.add_argument("--output_file", type=str, required=False, help="Path to the output file.")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose mode.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with the parsed arguments
    main(args)