import ast
from pathlib import Path

source = Path("instareels-downloader.py").read_text(encoding="utf-8")
ast.parse(source, filename="instareels-downloader.py")
updater = Path("updater.py").read_text(encoding="utf-8")
assert "urlsplit" in source and "urlunsplit" in source
assert "parsed.scheme != \"https\"" in source
assert "noplaylist" in source
assert "restrictfilenames" in source
assert "max_filesize" in source
assert "%(title).180s.%(ext)s" in source
assert "shell=True" not in source + updater
assert "safe_extract_zip(z, ext_dir)" in updater
assert "z.extractall(ext_dir)" not in updater
print("INSTAREELS_STATIC_SECURITY_CHECK_OK")
