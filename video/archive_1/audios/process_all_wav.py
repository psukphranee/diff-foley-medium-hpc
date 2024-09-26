import librosa
import numpy as np
import os
import sys
import subprocess

# Use the find command to locate wav2spec.py in the specified directory
try:
    # Run the find command to search for wav2spec.py in ~/Diff-Foley
    result = subprocess.run(['find', os.path.expanduser('~/Diff-Foley'), '-name', 'wav2spec.py'], 
                            capture_output=True, text=True, check=True)
    wav2spec_path = result.stdout.splitlines()[0]  # Get the first result from find command
    wav2spec_dir = os.path.dirname(wav2spec_path)  # Extract the directory of wav2spec.py
    sys.path.append(wav2spec_dir)  # Add the directory to sys.path

    # Import the MelSpectrogram class from wav2spec.py
    from wav2spec import MelSpectrogram

except (IndexError, subprocess.CalledProcessError):
    print("Error: Could not find wav2spec.py in ~/Diff-Foley. Make sure it exists in the specified directory.")
    sys.exit(1)

# Get all WAV files in the current directory
wav_files = [file for file in os.listdir('.') if file.endswith('.wav')]

# Define parameters for the MelSpectrogram
mel_spec_params = {
    'nfft': 2048,            # Number of FFT components
    'fmin': 0,               # Minimum frequency
    'nmels': 128,            # Number of Mel bands
    'hoplen': 512,           # Hop length
    'spec_power': 2.0        # Power to apply to spectrogram (e.g., 2.0 for power spectrogram)
}

# Loop through each WAV file and process it
for audio_file in wav_files:
    print(f"Processing {audio_file}...")

    # Load the WAV file
    y, sr = librosa.load(audio_file, sr=None)  # Load audio with the original sample rate

    # Initialize the MelSpectrogram with the loaded sample rate
    mel_spec = MelSpectrogram(sr=sr, fmax=sr // 2, **mel_spec_params)

    # Generate the Mel spectrogram
    mel_spectrogram = mel_spec(y)

    # Create the output file name by replacing the .wav extension with .npy
    output_file = os.path.splitext(audio_file)[0] + '.npy'

    # Save the spectrogram as a .npy file
    np.save(output_file, mel_spectrogram)

    print(f"Spectrogram saved as {output_file}")
