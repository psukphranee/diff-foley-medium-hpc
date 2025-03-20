import os
import subprocess
import sys

def resize_videos(directory, width=224, height=224):
    for filename in os.listdir(directory):
        if filename.lower().endswith(".mp4"):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, f"resized_{filename}")
            
            command = [
                "ffmpeg", "-i", input_path,
                "-vf", f"scale={width}:{height}",
                "-c:a", "copy", output_path
            ]
            
            subprocess.run(command, check=True)
            print(f"Resized: {filename} -> {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_directory>")
        sys.exit(1)
    
    input_directory = sys.argv[1]
    if not os.path.isdir(input_directory):
        print("Error: Provided path is not a directory.")
        sys.exit(1)
    
    resize_videos(input_directory)

