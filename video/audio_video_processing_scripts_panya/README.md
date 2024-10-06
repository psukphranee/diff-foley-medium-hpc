Converting A.2 Data Preprocessing to Checklist and Detail Implementation

1. Resample videos to 4 fps
   1. use "resample_to_4_fps.py"
2. Resize video to 224x224
3. Sample audio @ 16KHz and transform to melspec
   1. use "extract_wav_from_mp4.py"
   2. use "wav_to_spec_script.py". Need to specify hop 250 in wav2spec.py
4. Check Mel-Spec is 640x128 (T' x M)