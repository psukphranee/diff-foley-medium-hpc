import os
import sys
import subprocess

def extract_audio(input_directory):
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
            
            # FFmpeg command to extract audio and save as WAV with 16 kHz sampling rate
            command = [
                'ffmpeg', '-i', input_path, '-vn', '-acodec', 'pcm_s16le',
                '-ar', '16000', '-ac', '2', output_path
            ]
            
            print(f"Running FFmpeg command to extract audio:\n{' '.join(command)}")

            # Run the command
            subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Extracted: {output_path}")

    print("All MP4 files have been processed.")

# Main block to run the script with arguments
if __name__ == "__main__":
    # Check if the input directory is provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python extract_audio.py <input_directory>")
    else:
        input_directory = sys.argv[1]
        
        # Check if the specified directory exists
        if os.path.isdir(input_directory):
            extract_audio(input_directory)
        else:
            print(f"The directory '{input_directory}' does not exist. Please provide a valid directory.")

