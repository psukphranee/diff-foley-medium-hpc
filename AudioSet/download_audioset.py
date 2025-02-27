import pandas as pd
import os
from yt_dlp import YoutubeDL

print("Starting script...")


def download_from_csv(csv_file, output_dir):
    print(f"Reading CSV file: {csv_file}")
    df = pd.read_csv(csv_file, sep=',', quotechar='"', on_bad_lines='skip')  # Handle quoted fields
    # df = pd.read_csv(csv_file, sep=',', quotechar='"', on_bad_lines='skip', engine='python')  # Added engine='python'
    print(f"Found {len(df)} entries in CSV file")
    os.makedirs(output_dir, exist_ok=True)

    for youtube_id in df['YTID'].values:
        print(f"Downloading video with ID: {youtube_id}")
        try:
            download_video(youtube_id, output_dir)
            print(f"Successfully downloaded: {youtube_id}")
        except Exception as e:
            print(f"Failed to download {youtube_id}: {e}")

# Example: Load the CSV file and download the videos
# df = pd.read_csv('./balanced_train_segments.csv')
# output_dir = 'audioset_downloads'
# os.makedirs(output_dir, exist_ok=True)

for youtube_id in df['YTID'].values:
    download_video(youtube_id, output_dir)
