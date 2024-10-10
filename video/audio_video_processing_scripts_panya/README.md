Converting A.2 Data Preprocessing to Checklist and Detail Implementation

1. Resample videos to 4 fps
   1. use "resample_to_4_fps.py"
2. Resize video to 224x224
   1. 10.5.24 - in goodarchive_1.tar, videos are of different shapes
   2. transform_video() in data.py usees torchvision to reshape videos. Functions where transform_video() is called:
      1. cut_video_and_spec_filter
      2. cut_video_and_spec_bias
      3. cut_video_and_spec_vggsound_audioset
      4. cut_video_and_spec_vggsound_audioset_temporal_contrast
         1. called from preprocess_vggsound_audioset_temporal_contrast
      5. cut_video_and_spec_temporal_contrast
      6. cut_video_and_spec
3. Sample audio @ 16KHz and transform to melspec
   1. use "extract_wav_from_mp4.py"
   2. use "wav_to_spec_script.py". Need to specify hop 250 in wav2spec.py
4. Check Mel-Spec is 640x128 (T' x M)



cut_video_and_spec_vggsound_audioset_temporal_contrast(video, spec, sample_num=4, shift_lb=8)
-is video the mp4 binary and not an npy file? maybe its a binary of the mp4. but how do we reshape this?
- ANSWER: It IS A NPY VIDEO format

Try making another archive without the video.jpg as an .npy
