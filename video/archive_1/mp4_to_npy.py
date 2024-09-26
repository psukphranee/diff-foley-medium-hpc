import cv2
import numpy as np
import os

# Create output directory if it doesn't exist
output_dir = 'video_npy'
os.makedirs(output_dir, exist_ok=True)

# Get all mp4 files in the current directory
video_files = [f for f in os.listdir('.') if f.endswith('.mp4')]

for video_file in video_files:
    # Open the video file
    cap = cv2.VideoCapture(video_file)
    
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

print("Conversion completed. All .npy files are saved in the 'video_npy' folder.")
