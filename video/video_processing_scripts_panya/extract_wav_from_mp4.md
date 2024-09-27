Here’s the README in Markdown format:

```markdown
# Audio Extraction Script

This script extracts WAV audio files from all MP4 videos in a specified directory and saves them to a folder called `extracted_wav` within the same directory. The extracted audio is sampled at 16 kHz.

## Requirements

1. **Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. **FFmpeg**: This script uses FFmpeg to extract audio. You need to have FFmpeg installed and accessible from the command line.

### FFmpeg Installation

- **Windows**: Download FFmpeg from the [FFmpeg website](https://ffmpeg.org/download.html), and follow the installation instructions. Ensure FFmpeg is added to your system's PATH.
- **MacOS**: Use Homebrew to install FFmpeg:
  ```bash
  brew install ffmpeg
  ```
- **Linux (Ubuntu/Debian)**: Install FFmpeg using:
  ```bash
  sudo apt-get install ffmpeg
  ```

## How to Use the Script

### 1. Download the Script

Save the script as `extract_audio.py` in a location on your computer.

### 2. Run the Script

Open a terminal or command prompt, navigate to the directory containing the `extract_audio.py` script, and run the script with the path to the directory containing your MP4 files as an argument.

```bash
python extract_audio.py <path/to/your/directory>
```

### Example

If your MP4 files are stored in a folder located at `C:\Users\YourUsername\Videos`, you would run:

```bash
python extract_audio.py C:\Users\YourUsername\Videos
```

Or on Mac/Linux:

```bash
python extract_audio.py /Users/YourUsername/Videos
```

### 3. Output

- The script will create an `extracted_wav` folder within the specified input directory.
- Extracted WAV files will be saved in this folder, each with the same name as the original MP4 but with a `.wav` extension.

## Script Overview

- **Input Directory**: Specified when running the script. Contains the MP4 files to process.
- **Output Directory**: A subdirectory named `extracted_wav` inside the input directory.
- **Audio Format**: Extracted audio is saved in WAV format, sampled at 16 kHz.

### Error Handling

- If the input directory is not specified or does not exist, the script will prompt you to provide a valid directory.

## Troubleshooting

- **FFmpeg Not Found**: Ensure FFmpeg is installed correctly and added to your system's PATH.
- **Permission Denied**: If you encounter permission issues, ensure you have the necessary rights to read from the input directory and write to the output directory.

## License

This script is provided as-is without any warranties. You are free to use, modify, and distribute it.
```

