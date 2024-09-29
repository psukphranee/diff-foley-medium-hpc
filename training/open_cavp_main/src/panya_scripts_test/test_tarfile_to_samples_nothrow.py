import sys
import os
import webdataset as wds

# Step 1: Import the necessary files
# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../training/')))

from data import tarfile_to_samples_nothrow  # Assuming data.py is in the parent directory

# Step 2: Define the URL (or list of URLs) for your tar file(s)
url = "/Users/920753844/Diff-Foley/video/goodarchive_1.tar"

# Step 3: Create the DataPipeline with tarfile_to_samples_nothrow
dataset = wds.DataPipeline(
    wds.SimpleShardList([url]),  # Use a list of shards if multiple shards are available
    tarfile_to_samples_nothrow   # Use your custom implementation
)

# Step 4: Create a WebLoader to iterate through the dataset
loader = wds.WebLoader(dataset, batch_size=None)

# Step 5: Iterate through the dataset
for sample in loader:
    print("Panya: key=",sample["__key__"], " | url=", sample["__url__"])
    