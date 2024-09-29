import cv2
import numpy as np
import os
import sys

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

# Create output directory if it doesn't exist
output_dir = os.path.join(input_directory, 'video_npy')
os.makedirs(output_dir, exist_ok=True)
print(f"Output directory '{output_dir}' created or already exists.")

# Get all mp4 files in the specified input directory
video_files = [f for f in os.listdir(input_directory) if f.endswith('.mp4')]

if not video_files:
    print("No .mp4 files found in the specified directory.")
    sys.exit(1)

print(f"Found {len(video_files)} .mp4 file(s) in '{input_directory}'.")

for video_file in video_files:
    print(f"Processing video: {video_file}")
    # Open the video file
    video_path = os.path.join(input_directory, video_file)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video file '{video_file}'. Skipping...")
        continue

    frames = []
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print(f"End of video reached or error reading frame from '{video_file}'.")
            break
        # Convert frame to RGB if needed and append it to frames list
        frames.append(frame)
        frame_count += 1

    # Release the video capture object
    cap.release()

    if frame_count == 0:
        print(f"No frames extracted from '{video_file}'. Skipping...")
        continue

    print(f"Extracted {frame_count} frame(s) from '{video_file}'.")

    # Convert the list of frames to a numpy array
    frames_array = np.array(frames)
    
    # Create the output file name by replacing .mp4 with .npy
    output_file = os.path.join(output_dir, os.path.splitext(video_file)[0] + '.npy')
    
    # Save the frames array as .npy file
    np.save(output_file, frames_array)
    print(f"Saved '{output_file}' with shape {frames_array.shape}.")

print(f"Conversion completed. All .npy files are saved in the '{output_dir}' folder.")
