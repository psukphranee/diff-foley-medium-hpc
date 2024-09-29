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
  # Check if the file name starts with an underscore or other specific special characters
  if [[ "$file" =~ ^[_]+ ]]; then
    # Generate a new file name by removing leading underscores
    new_file=$(echo "$file" | sed 's/^_+//')
    
    # Check if new file name is empty to avoid renaming to an empty string
    if [ -z "$new_file" ]; then
      echo "Cannot rename '$file' because the new filename would be empty."
      continue
    fi

    # Rename the file using -- to handle filenames starting with special characters
    mv -- "$file" "$new_file" || { echo "Failed to rename '$file'"; continue; }
    
    # Print the old and new file names
    echo "Renamed: '$file' -> '$new_file'"
  else
    # Print message if file does not start with the targeted special character
    echo "'$file' does not start with the targeted special character."
  fi
done

echo "Renaming complete."

