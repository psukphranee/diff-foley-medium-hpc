#!/bin/bash

# Directory containing the input files
INPUT_DIR="."  # Set this to the directory containing your .mp4 files
OUTPUT_DIR="./audios" # Set this to your desired output directory

# Ensure the output directory exists
mkdir -p "$OUTPUT_DIR"

# Loop through all .mp4 files in the input directory
for input_file in "$INPUT_DIR"/*.mp4; do
    # Extract the base name of the file without the extension
    base_name=$(basename "$input_file" .mp4)

    # Set the output file name with the same base name and .wav extension
    output_file="$OUTPUT_DIR/${base_name}.wav"

    # Run the command for each file
    echo "Extracting audio from $input_file to $output_file"
    audio-extract --input="$input_file" --output="$output_file" --format="wav"
done

echo "Completed all extractions."

