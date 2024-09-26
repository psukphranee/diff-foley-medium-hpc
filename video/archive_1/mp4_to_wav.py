import os
import subprocess

# Define the current directory as the input directory
input_directory = os.path.dirname(os.path.abspath(__file__))

# Define the output directory for extracted WAV files
output_directory = os.path.join(input_directory, 'extracted_wav')

# Create the output directory if it does not exist
os.makedirs(output_directory, exist_ok=True)

# Loop through each file in the input directory
for filename in os.listdir(input_directory):
    if filename.lower().endswith('.mp4'):
        # Construct full input path
        input_path = os.path.join(input_directory, filename)
        
        # Construct output path and change the extension to .wav
        output_filename = os.path.splitext(filename)[0] + '.wav'
        output_path = os.path.join(output_directory, output_filename)
        
        # FFmpeg command to extract audio and save as WAV
        command = [
            'ffmpeg', '-i', input_path, '-vn', '-acodec', 'pcm_s16le',
            '-ar', '44100', '-ac', '2', output_path
        ]
        
        # Run the command
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Extracted: {output_path}")

print("All MP4 files have been processed.")
