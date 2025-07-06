import os, yt_dlp
from yt_dlp import YoutubeDL

# Credit to STACK OVERFLOW Alexander McFarlane
def get_download_path():
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

def download(url):
    output = get_download_path()
    ydl_opts = {
        "format": "mp3/bestaudio/best",
        "outtmpl": output + "\\%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as dlp:
        dlp.extract_info(video_url, download=True)

while True:
    video_url = input("Enter YouTube video URL: ").strip()
    if video_url.startswith("https://"):
        download(video_url)
        break
    else:
        print("Invalid URL. Please try again.")
