import os
import json
import tarfile

def count_samples_in_shard(shard_path):
    """
    Count the number of samples in a given shard (tar file).

    Args:
        shard_path (str): Path to the shard file.

    Returns:
        int: The number of samples in the shard.
    """
    try:
        with tarfile.open(shard_path, 'r') as tar:
            # Assuming each file inside tar corresponds to a sample
            return len(tar.getmembers())
    except Exception as e:
        print(f"Error processing {shard_path}: {e}")
        return 0

def generate_sizes_json(directory):
    """
    Searches for shard files in the given directory and creates a sizes.json file.

    Args:
        directory (str): Directory to search for shard files.
    """
    # List all .tar files in the current directory as potential shards
    shard_files = [f for f in os.listdir(directory) if f.endswith('.tar')]
    sizes = {}

    # Count samples in each shard and store in the sizes dictionary
    for shard_file in shard_files:
        shard_path = os.path.join(directory, shard_file)
        sample_count = count_samples_in_shard(shard_path)
        sizes[shard_file] = sample_count
        print(f"Processed {shard_file}: {sample_count} samples")

    # Save sizes.json in the current directory
    sizes_filename = os.path.join(directory, 'sizes.json')
    with open(sizes_filename, 'w') as f:
        json.dump(sizes, f)

    print(f"sizes.json created at {sizes_filename}")

if __name__ == "__main__":
    # Use the current directory where the script is running
    current_directory = os.getcwd()
    generate_sizes_json(current_directory)
