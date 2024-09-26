#!/bin/bash

# Get the directory of the script
directory="$(dirname "$0")"

# Change to the script's directory
cd "$directory" || exit

# Loop through all files in the directory
for file in *; do
  # Check if the file name starts with a dash
  if [[ "$file" == -* ]]; then
    # Generate a new file name by removing the leading dash, handling special characters safely
    new_file="${file#-}"

    # Use mv with -- to handle filenames with special characters safely
    mv -- "$file" "$new_file"
    
    # Print the old and new file names
    echo "Renamed: '$file' -> '$new_file'"
  else
    # Print message if file does not start with a dash
    echo "'$file' does not start with a dash."
  fi
done

echo "Renaming complete."

