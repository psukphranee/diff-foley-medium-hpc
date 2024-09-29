#!/bin/bash

# Check if an input directory is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

# Use the specified directory as the input directory
input_directory="$1"

# Check if the specified directory exists
if [ ! -d "$input_directory" ]; then
  echo "Error: Directory '$input_directory' does not exist."
  exit 1
fi

# Change to the specified directory
cd "$input_directory" || exit

# Loop through all files in the directory
for file in *; do
  # Check if the file name matches the pattern ending with _ followed by six digits before the file extension
  if [[ "$file" =~ _[0-9]{6}\.[a-zA-Z0-9]+$ ]]; then
    # Extract the base name without the underscore and digits, keeping the extension
    new_file=$(echo "$file" | sed -E 's/_[0-9]{6}(\.[a-zA-Z0-9]+)$/\1/')

    # Debug: Print the old and new file names to verify the match
    echo "Renaming: '$file' -> '$new_file'"

    # Rename the file (remove echo to actually rename)
    mv "$file" "$new_file"
  else
    # Debug: Print message if file doesn't match the pattern
    echo "'$file' does not match the pattern."
  fi
done

echo "Renaming complete."

