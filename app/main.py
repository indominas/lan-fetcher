from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse
from app.downloader import download
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    return open("app/templates/index.html").read()

@app.post("/fetch")
def fetch(url: str = Form(...), fmt: str = Form("mp4")):
    file_path = download(url, fmt)
    return FileResponse(
        path=file_path,
        filename=os.path.basename(file_path),
        media_type="application/octet-stream"
    )
