import sys
import os
from data import tarfile_to_samples_nothrow  # Assuming data.py is in the parent directory

# Step 1: Importing the necessary files
# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Step 2: Call tarfile_to_samples_nothrow with 'goodarchive_1.tar'
tar_file_path = '/Users/920753844/Diff-Foley/video/goodarchive_1.tar'

# Call the function with the tar file
samples = tarfile_to_samples_nothrow(tar_file_path)

# Step 3: Process and print the samples
for sample in samples:
    print(sample)

