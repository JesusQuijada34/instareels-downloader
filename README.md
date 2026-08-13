# InstaReels Downloader

**InstaReels Downloader** es una aplicación de escritorio fuente para Windows, Linux y macOS que permite seleccionar contenido público de Instagram y descargarlo mediante `yt-dlp`.

## Clasificación PackageMaker

El proyecto se distribuye como **AlphaCube** porque es código fuente multiplataforma basado en PyQt5, PyQtWebEngine y yt-dlp; no se presenta como un binario Linux Danenone ni como un instalador Windows ya compilado.

La aplicación solo acepta URLs HTTPS de `instagram.com`, `www.instagram.com` o `m.instagram.com` con rutas de Reel, publicación o TV. Las descargas son de una sola entrada, limitadas a 500 MB, con reintentos acotados y plantillas de salida saneadas por yt-dlp. Debes descargar únicamente contenido para el que tengas autorización y respetar los términos de servicio, derechos de autor y leyes aplicables.

## Características

- Navegador integrado para explorar Instagram.
- Detección automática de la URL del Reel, publicación o video de Instagram.
- Descarga de video en formato MP4.
- Descarga de audio en formato MP3.
- Selección de carpeta de destino para las descargas.
- Interfaz moderna y oscura.

## Requisitos

- Python 3.7 o superior
- [PyQt5](https://pypi.org/project/PyQt5/)
- [PyQtWebEngine](https://pypi.org/project/PyQtWebEngine/)
- [yt-dlp](https://pypi.org/project/yt-dlp/)

Puedes instalar las dependencias ejecutando:

```bash
python3 -m pip install -r lib/requirements.txt
python3 instareels-downloader.py
```

En sistemas Linux puede ser necesario instalar previamente Qt WebEngine y FFmpeg mediante el gestor de paquetes de la distribución.
