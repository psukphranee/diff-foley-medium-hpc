#!/bin/bash

# Loop through each line in commands.txt
while IFS= read -r line
do
  echo "Running command: $line"
  # Run the command
  $line
done < "encoding_commands.txt"
