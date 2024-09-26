import os
import numpy as np
import sys
import subprocess
import librosa
print(librosa.__version__)


# Use the find command to locate wav2spec.py in the specified directory
try:
    # Run the find command to search for wav2spec.py in ~/Diff-Foley
    result = subprocess.run(['find', os.path.expanduser('~/Documents/diff-foley-medium-hpc'), '-name', 'wav2spec.py'], 
                            capture_output=True, text=True, check=True)
    wav2spec_path = result.stdout.splitlines()[0]  # Get the first result from find command
    wav2spec_dir = os.path.dirname(wav2spec_path)  # Extract the directory of wav2spec.py
    sys.path.append(wav2spec_dir)  # Add the directory to sys.path

    # Import the get_spectrogram function from wav2spec.py
    from wav2spec import get_spectrogram

except (IndexError, subprocess.CalledProcessError):
    print("Error: Could not find wav2spec.py in ~/Diff-Foley. Make sure it exists in the specified directory.")
    sys.exit(1)

# Get all WAV files in the current directory
wav_files = [file for file in os.listdir('.') if file.endswith('.wav')]

# Loop through each WAV file and process it
for audio_file in wav_files:
    print(f"Processing {audio_file}...")

    # Get the spectrogram of the current WAV file
    spectrogram = get_spectrogram(audio_file, 10, 16000)

    # Create the output file name by replacing the .wav extension with .npy
    output_file = os.path.splitext(audio_file)[0] + '.npy'

    # Save the spectrogram as a .npy file
    np.save(output_file, spectrogram)

    print(f"Spectrogram saved as {output_file}")
