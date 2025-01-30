import os
from pytube import YouTube
from pydub import AudioSegment

def download_audio(url, output_folder="downloads"):
    os.makedirs(output_folder, exist_ok=True)
    try:
        print("Fetching video info...")
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        if not audio_stream:
            print("No audio stream found.")
            return None
        print(f"Downloading: {yt.title}")
        file_path = audio_stream.download(output_folder)
        mp3_path = os.path.splitext(file_path)[0] + ".mp3"
        print("Converting to MP3...")
        audio = AudioSegment.from_file(file_path)
        audio.export(mp3_path, format="mp3")
        os.remove(file_path)

        print(f"Done! Saved as: {mp3_path}")
        return mp3_path

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ").strip()
    if video_url:
        download_audio(video_url)
    else:
        print("Invalid URL. Please try again.")
