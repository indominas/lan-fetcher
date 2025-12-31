# 🌕 PROJECT: LAN Media Fetcher (LMF)

## Description
A self-hosted web app that:
* accepts YouTube / Instagram / many sites
* runs yt-dlp safely
* streams downloads to any device
* shows progress in real-time
* supports formats, audio-only, playlists
* caches downloads
* is LAN-locked
* looks 🔥

## 🧠 Final Architecture
```
Browser (any device)
  ↓
Nginx / Apache (reverse proxy)
  ↓
FastAPI (async backend)
  ↓
Task Queue (async worker)
  ↓
yt-dlp
  ↓
Cache + Stream to client
```

## 🔩 Tech Stack (Best-in-class)
**Layer**   **Choice**  **Why**
Frontend	HTML + JS (or React later)	Lightweight
Backend	FastAPI	Async, fast, typed
Worker	asyncio / background tasks	No blocking
Downloader	yt-dlp	Best tool
Server	Nginx or Apache	Reverse proxy
Security	IP filtering + auth	LAN safe
Storage	Temp + cache	Efficient
Format	MP4 / MP3	Universal

### 1️⃣ Project Structure
```
lan-fetcher/
├── app/
│   ├── main.py
│   ├── downloader.py
│   ├── models.py
│   └── templates/
│       └── index.html
├── downloads/
├── venv/
└── run.sh
```

### 2️⃣ Install Dependencies
```
pip install fastapi uvicorn yt-dlp aiofiles python-multipart
```

### 3️⃣ Core Downloader Logic (`downloader.py`)
### 4️⃣ FastAPI Backend (`main.py`)
### 5️⃣ Frontend (`index.html`)
### 6️⃣ Run It
```
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
Access from any device
```
http://LAN_IP:8000
```
