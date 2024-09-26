#!/bin/bash

# Get the directory of the script
directory="$(dirname "$0")"

# Change to the script's directory
cd "$directory" || exit

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

