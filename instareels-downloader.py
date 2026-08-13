import sys
import os
from urllib.parse import urlsplit, urlunsplit
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QLineEdit, QFileDialog, QMessageBox
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
        self.url_field.setText(self.format_url(qurl.toString()))

    @staticmethod
    def format_url(url):
        """Return only canonical HTTPS Instagram content URLs."""
        try:
            parsed = urlsplit(url.strip())
        except ValueError:
            return ""
        host = (parsed.hostname or "").lower().rstrip(".")
        if parsed.scheme != "https" or host not in {"instagram.com", "www.instagram.com", "m.instagram.com"}:
            return ""
        parts = [part for part in parsed.path.split("/") if part]
        if len(parts) < 2 or parts[0] not in {"reel", "p", "tv"}:
            return ""
        return urlunsplit(("https", "www.instagram.com", "/" + "/".join(parts[:2]), "", ""))

    def selected_url(self):
        url = self.format_url(self.url_field.text())
        if not url:
            QMessageBox.warning(self, "URL no válida", "Selecciona un Reel, publicación o vídeo HTTPS de Instagram.")
        return url

    @staticmethod
    def download_options(output_template, format_spec):
        return {
            "format": format_spec,
            "outtmpl": output_template,
            "noplaylist": True,
            "restrictfilenames": True,
            "windowsfilenames": True,
            "max_filesize": 500 * 1024 * 1024,
            "socket_timeout": 30,
            "retries": 3,
            "quiet": True,
            "no_warnings": True,
        }

    def change_path(self):
        folder = QFileDialog.getExistingDirectory(self, "Selecciona carpeta de descarga")
        if folder:
            self.download_path = folder

    def download_audio(self):
        url = self.selected_url()
        if not url:
            return
        destination = Path(self.download_path or Path.home() / "Music" / "Instagram")
        destination.mkdir(parents=True, exist_ok=True)
        output = str(destination / "%(title).180s.%(ext)s")
        opts = self.download_options(output, "bestaudio/best")
        opts["postprocessors"] = [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
        try:
            with YoutubeDL(opts) as ydl:
                ydl.download([url])
        except Exception as error:
            QMessageBox.critical(self, "Descarga fallida", str(error)[:500])

    def download_video(self):
        url = self.selected_url()
        if not url:
            return
        destination = Path(self.download_path or Path.home() / "Videos" / "Instagram")
        destination.mkdir(parents=True, exist_ok=True)
        output = str(destination / "%(title).180s.%(ext)s")
        opts = self.download_options(output, "best")
        try:
            with YoutubeDL(opts) as ydl:
                ydl.download([url])
        except Exception as error:
            QMessageBox.critical(self, "Descarga fallida", str(error)[:500])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InstaReelsDownloader()
    window.show()
    sys.exit(app.exec_())