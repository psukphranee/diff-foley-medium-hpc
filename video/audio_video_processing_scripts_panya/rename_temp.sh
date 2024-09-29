#!/bin/bash

# Check if the input directory is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 /path/to/directory"
  exit 1
fi

# Set the input directory to the first argument
directory="$1"

# Change to the specified directory
cd "$directory" || { echo "Directory not found: $directory"; exit 1; }

# Loop through all files ending with _resampled
for file in *"_resampled"*; do
  # Check if the file ends with _resampled
  if [[ "$file" == *"_resampled"* ]]; then
    # Generate the new file name by replacing _resampled with RESAMPLED4FPS
    new_file=$(echo "$file" | sed 's/_resampled/RESAMPLED4FPS/')

    # Rename the file
    mv -- "$file" "$new_file" || { echo "Failed to rename '$file'"; continue; }

    # Print the old and new file names
    echo "Renamed: '$file' -> '$new_file'"
  else
    # Print message if file does not match the pattern
    echo "'$file' does not end with _resampled."
  fi
done

echo "Renaming complete."

