import os
import numpy as np
import librosa
import soundfile as sf
import subprocess

def extract_audio_from_video(video_path, audio_output_path):
    """
    Extract audio from a video file using ffmpeg.

    Args:
        video_path (str): Path to the input video file.
        audio_output_path (str): Path to save the extracted audio file.
    """
    command = f"ffmpeg -i \"{video_path}\" -q:a 0 -map a \"{audio_output_path}\" -y"
    subprocess.run(command, shell=True, check=True)
    print(f"Audio extracted and saved to {audio_output_path}")

def generate_mel_spectrogram(audio_path, sr=16000, n_fft=1024, hop_length=512, n_mels=128):
    """
    Generate a Mel-spectrogram from an audio file.

    Args:
        audio_path (str): Path to the audio file.
        sr (int): Sampling rate for the audio.
        n_fft (int): Number of FFT components.
        hop_length (int): Number of samples between successive frames.
        n_mels (int): Number of Mel bands.

    Returns:
        np.ndarray: The generated Mel-spectrogram.
    """
    # Load the audio file
    y, sr = librosa.load(audio_path, sr=sr)
    
    # Compute the Mel-spectrogram
    mel_spec = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels)
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)
    
    return mel_spec_db

def save_mel_spectrogram(mel_spec, output_path):
    """
    Save the Mel-spectrogram as a .npy file.

    Args:
        mel_spec (np.ndarray): The Mel-spectrogram array.
        output_path (str): Path to save the .npy file.
    """
    np.save(output_path, mel_spec)
    print(f"Mel-spectrogram saved at {output_path}")

def process_videos(videos_dir, output_dir):
    """
    Process each video in the directory to generate and save Mel-spectrograms.

    Args:
        videos_dir (str): Directory containing the video files.
        output_dir (str): Directory to save the generated Mel-spectrograms.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file in os.listdir(videos_dir):
        if file.endswith((".mp4", ".mkv", ".avi")):  # Modify extensions based on your video format
            video_path = os.path.join(videos_dir, file)
            audio_path = os.path.join(output_dir, file.replace('.mp4', '.wav'))  # Change extension as needed
            
            # Extract audio from the video
            extract_audio_from_video(video_path, audio_path)
            
            # Generate Mel-spectrogram from the extracted audio
            mel_spec = generate_mel_spectrogram(audio_path)
            
            # Save the Mel-spectrogram as a .npy file
            spec_output_path = os.path.join(output_dir, file.replace('.mp4', '_mel.npy'))
            save_mel_spectrogram(mel_spec, spec_output_path)

if __name__ == "__main__":
    videos_dir = "."  # Directory containing your video files
    output_dir = "./mel-specs"  # Directory to save generated Mel-spectrograms
    process_videos(videos_dir, output_dir)
