import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QLineEdit, QFileDialog
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt, QUrl
from yt_dlp import YoutubeDL
from pathlib import Path

class InstaReelsDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("InstaReels Downloader")
        self.setGeometry(100, 100, 1000, 600)
        self.setStyleSheet("""
            QWidget {
                background-color: #0d1117;
                color: #c9d1d9;
                font-family: Arial;
                font-size: 11pt;
                border: 1px solid #30363d;
                border-radius: 3px;
            }
            QPushButton {
                background-color: #161b22;
                border: none;
                padding: 6px;
                font-weight: bold;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #21262d;
            }
            QPushButton:pressed {
                background-color: #30363d;
            }
            QLineEdit {
                background-color: #161b22;
                border: 1px solid #30363d;
                color: #c9d1d9;
                padding: 4px;
            }
        """)

        # Navegador embebido
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.instagram.com"))
        self.browser.urlChanged.connect(self.capture_url)

        # Panel lateral
        self.url_label = QLabel("🔗 URL detectada:")
        self.url_field = QLineEdit()
        self.url_field.setReadOnly(True)

        self.download_audio_btn = QPushButton("Descargar Audio")
        self.download_audio_btn.clicked.connect(self.download_audio)

        self.download_video_btn = QPushButton("Descargar Video")
        self.download_video_btn.clicked.connect(self.download_video)

        self.path_btn = QPushButton("Cambiar carpeta")
        self.path_btn.clicked.connect(self.change_path)

        self.download_path = str(Path.home() / "Downloads")

        side_layout = QVBoxLayout()
        side_layout.addWidget(self.url_label)
        side_layout.addWidget(self.url_field)
        side_layout.addWidget(self.download_audio_btn)
        side_layout.addWidget(self.download_video_btn)
        side_layout.addWidget(self.path_btn)

        main_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.browser, 3)
        top_layout.addLayout(side_layout, 1)

        main_layout.addLayout(top_layout)
        self.setLayout(main_layout)

    def capture_url(self, qurl):
        raw_url = qurl.toString()
        clean_url = self.format_url(raw_url)
        self.url_field.setText(clean_url)

    def format_url(self, url):
        if "instagram.com/reel/" in url or "instagram.com/p/" in url or "instagram.com/tv/" in url:
            return url.split("?")[0]
        return url

    def change_path(self):
        folder = QFileDialog.getExistingDirectory(self, "Selecciona carpeta de descarga")
        if folder:
            self.download_path = folder

    def get_title(self, url):
        try:
            with YoutubeDL({'quiet': True}) as ydl:
                info = ydl.extract_info(url, download=False)
                return info.get('title', 'insta_media')
        except Exception:
            return "insta_media"

    def download_audio(self):
        url = self.url_field.text()
        title = self.get_title(url)
        output = os.path.join(self.download_path or str(Path.home() / "Music" / "Instagram"), f"{title}.mp3")
        opts = {
            'format': 'bestaudio/best',
            'outtmpl': output,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with YoutubeDL(opts) as ydl:
            ydl.download([url])

    def download_video(self):
        url = self.url_field.text()
        title = self.get_title(url)
        output = os.path.join(self.download_path or str(Path.home() / "Videos" / "Instagram"), f"{title}.mp4")
        opts = {
            'format': 'best',
            'outtmpl': output,
        }
        with YoutubeDL(opts) as ydl:
            ydl.download([url])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InstaReelsDownloader()
    window.show()
    sys.exit(app.exec_())