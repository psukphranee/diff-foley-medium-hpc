import os
import numpy as np
import sys
import subprocess
import argparse

# Set up argument parser to get the input directory from the command line
parser = argparse.ArgumentParser(description="Process WAV files in the specified directory to generate spectrograms.")
parser.add_argument('input_dir', type=str, help='Path to the directory containing WAV files')

# Parse the arguments
args = parser.parse_args()

# Get the input directory from the parsed arguments
input_dir = args.input_dir

# Check if the input directory exists
if not os.path.isdir(input_dir):
    print(f"Error: The directory {input_dir} does not exist.")
    sys.exit(1)

# Use the find command to locate wav2spec.py in the specified directory

try:
    # PANYA READ: change path depending on computer your on
    result = subprocess.run(['find', os.path.expanduser('.'],
                            capture_output=True, text=True, check=True)
    wav2spec_path = result.stdout.splitlines()[0]  # Get the first result from find command
    wav2spec_dir = os.path.dirname(wav2spec_path)  # Extract the directory of wav2spec.py
    sys.path.append(wav2spec_dir)  # Add the directory to sys.path

    # Import the get_spectrogram function from wav2spec.py
    from wav2spec import get_spectrogram

except (IndexError, subprocess.CalledProcessError):
    print("Error: Could not find wav2spec.py in ~/Documents/diff-foley-medium-hpc. Make sure it exists in the specified directory.")
    print("PANYA READ: change path depending on computer your on.")
    sys.exit(1)

# Get all WAV files in the specified input directory
wav_files = [file for file in os.listdir(input_dir) if file.endswith('.wav')]

# Check if there are any WAV files to process
if not wav_files:
    print(f"No WAV files found in {input_dir}.")
    sys.exit(1)

# Loop through each WAV file and process it
for audio_file in wav_files:
    audio_path = os.path.join(input_dir, audio_file)
    print(f"Processing {audio_path}...")

    # Get the spectrogram of the current WAV file
    _, spectrogram = get_spectrogram(audio_path, length=16000*10, sr=16000)  # Adjust length and sr as needed

    # Create the output file name by replacing the .wav extension with .npy
    output_file = os.path.splitext(audio_file)[0] + '.npy'
    output_path = os.path.join(input_dir, output_file)

    # Save the spectrogram as a .npy file
    np.save(output_path, spectrogram)

    print(f"Spectrogram saved as {output_path}")
