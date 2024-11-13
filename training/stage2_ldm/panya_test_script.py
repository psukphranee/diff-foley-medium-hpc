# Goal is to use the Stage 1 CAVP to extract features from video


# test_decoder_wrapper.py
import torch
import importlib.util
import os

# Path to clip_video_spec.py file
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'adm', 'modules', 'stage2_decode', 'clip_video_spec.py'))

# Load the module
spec = importlib.util.spec_from_file_location("clip_video_spec", module_path)
clip_video_spec = importlib.util.module_from_spec(spec)
spec.loader.exec_module(clip_video_spec)

# Access the CLIP_Video_Spec_v2 class
CLIP_Video_Spec_v2 = clip_video_spec.CLIP_Video_Spec_v2


first_stage_ckpt = '/Users/920753844/Diff-Foley/training/open_cavp_main/logs/2024_10_21-14_32_19-lr_8e-4_warmup200_wds_vgg+audioset_cnn14_pretrained_clip_num3_shift_lb8_intra_loss_w1/checkpoints/epoch_latest.pt'

slowonly_path = "/Users/920753844/Diff-Foley/training/open_cavp_main/src/pretrained_model/slowonly_r50_4x16x1_256e_8xb16_kinetics400-rgb_20220901-f6a40d08.pth"

def test_clip_video_spec_v2():
    # Parameters
    embed_dim = 512  # embedding dimension for the projection head
    video_encode = "Slowonly"
    spec_encode = "resnet50"
    use_spec_aug = False
    video_pretrained = True
    audio_pretrained = False
    
    # Initialize model with mock encoders
    model = CLIP_Video_Spec_v2(
        video_encode=video_encode,
        spec_encode=spec_encode,
        embed_dim=embed_dim,
        use_spec_aug=use_spec_aug,
        video_pretrained=video_pretrained,
        audio_pretrained=audio_pretrained
    )
    
    # Randomly generated input tensors for testing
    video_input = torch.rand(batch_size, time_steps, 3, video_height, video_width)  # [B, T, C, H, W]
    spec_input = torch.rand(batch_size, mel_bins, spec_time_steps)                 # [B, Mel_bins, T]

    # Forward pass through the model
    output = model(video_input, spec_input)
    
    # Print output to verify
    print("Video Features:", output["video_features"].shape)
    print("Spec Features:", output["spec_features"].shape)
    print("Logit Scale:", output["logit_scale"].item())


if __name__ == "__main__":
    test_clip_video_spec_v2()
