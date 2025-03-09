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

# Get all mp4 files in the specified input directory
video_files = [f for f in os.listdir(input_directory) if f.endswith('.mp4')]

for video_file in video_files:
    # Open the video file
    video_path = os.path.join(input_directory, video_file)
    cap = cv2.VideoCapture(video_path)
    
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Convert frame to RGB if needed and append it to frames list
        frames.append(frame)
    
    # Release the video capture object
    cap.release()
    
    # Convert the list of frames to a numpy array
    frames_array = np.array(frames)
    
    # Create the output file name by replacing .mp4 with .npy
    output_file = os.path.join(output_dir, os.path.splitext(video_file)[0] + '.npy')
    
    # Save the frames array as .npy file
    np.save(output_file, frames_array)

print(f"Conversion completed. All .npy files are saved in the '{output_dir}' folder.")

