import yt_dlp
import uuid
from pathlib import Path

DOWNLOAD_DIR = Path("downloads")
DOWNLOAD_DIR.mkdir(exist_ok=True)

def download(url: str, fmt: str):
    uid = uuid.uuid4().hex
    outtmpl = DOWNLOAD_DIR / f"{uid}.%(ext)s"

    ydl_opts = {
        "outtmpl": str(outtmpl),
        "format": "bestaudio/best" if fmt == "mp3" else "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)
