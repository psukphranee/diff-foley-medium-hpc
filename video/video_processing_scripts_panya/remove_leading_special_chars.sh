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

# Loop through all files in the directory
for file in *; do
  # Check if the file name starts with a special character
  if [[ "$file" =~ ^[[:punct:]]+ ]]; then
    # Generate a new file name by removing leading special characters
    new_file=$(echo "$file" | sed 's/^[[:punct:]]\+//')
    
    # Rename the file using -- to handle filenames starting with special characters
    mv -- "$file" "$new_file"
    
    # Print the old and new file names
    echo "Renamed: '$file' -> '$new_file'"
  else
    # Print message if file does not start with a special character
    echo "'$file' does not start with a special character."
  fi
done

echo "Renaming complete."

