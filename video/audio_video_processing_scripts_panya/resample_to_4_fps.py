import os
import sys
import subprocess

# Set the frame rate for resampling
FRAME_RATE = 4  # Change as needed

# Check if an input directory is provided as an argument
if len(sys.argv) < 2:
    print("Usage: python script.py <input_directory>")
    sys.exit(1)

# Use the specified directory as the input directory
input_directory = sys.argv[1]

# Check if the specified directory exists
if not os.path.isdir(input_directory):
    print(f"Error: Directory '{input_directory}' does not exist.")
    sys.exit(1)

# List all MP4 files in the directory
mp4_files = [f for f in os.listdir(input_directory) if f.endswith('.mp4')]

# Create a directory for the output files
output_directory = os.path.join(input_directory, 'output_resampled_4fps')
os.makedirs(output_directory, exist_ok=True)

# Process each MP4 file
for file in mp4_files:
    # Construct full input path
    input_path = os.path.join(input_directory, file)
    
    # Define output file name for resampled video
    basename = os.path.splitext(file)[0]
    resampled_file = os.path.join(output_directory, f"{basename}_resampled.mp4")

    # Step 1: Resample the video to 4 fps
    resample_command = [
        'ffmpeg', '-v', 'verbose', '-i', input_path, '-r', str(FRAME_RATE), resampled_file
    ]
    subprocess.run(resample_command, check=True)

    # Optional: Remove the intermediate resampled file to save space
    # os.remove(resampled_file)

print("Processing complete!")

