# InstaReels Downloader

**Identidad del paquete:** `influent.instareels-downloader.v1.0-26.08-21.56`
**Autor:** `JesusQuijada34`
**Plataforma:** `AlphaCube`
**Descripción:** Estructura reparada por MoonFix

## Estructura PackageMaker 3.2.7

Este repositorio fue normalizado mediante **MoonFix**, usando la estructura de PackageMaker 3.2.7. El paquete público debe conservar `details.xml`, `version.res`, `autorun`, `autorun.bat`, `.storedetail`, `updater.py`, `config/settings.json`, los marcadores `.container` y los archivos de documentación correspondientes. El publisher oficial es `influent` y la versión pública no contiene sufijo de plataforma.

## Instalación y ejecución

Instala las dependencias declaradas en `lib/requirements.txt` cuando exista y ejecuta el entrypoint real del proyecto. En Linux, los comandos privilegiados son específicos de Danenone y no deben trasladarse a Windows. En proyectos AlphaCube, la validación Windows debe realizarse con el `buildthis` oficial de PackageMaker.

## Validación

La fuente debe pasar compilación sintáctica, pruebas funcionales disponibles, comprobación de identidad XML, protección contra traversal en ZIP y llamadas seguras a subprocess. Los artefactos `.iflapp` deben ser generados por PackageMaker; los paquetes Debian deben usar el nombre canónico `influent.instareels-downloader.v1.0-26.08-21.56_ARCH.deb`.

## Release

El tag y el título del release deben ser exactamente `v1.0-26.08-21.56`. Los assets deben usar el nombre canónico del paquete y una extensión objetiva. No se permite publicar un release AlphaCube que contenga únicamente el build Linux.

## Referencia original

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
