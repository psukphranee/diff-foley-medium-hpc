import os
import subprocess

# Set the frame rate and segment time
FRAME_RATE = 4
SEGMENT_TIME = 4

# Directory containing MP4 files
input_directory = '.'  # Use the current directory; change as needed

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

