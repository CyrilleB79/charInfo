# Technical notes

## How to update unicodedata2 package?

To update unicodedata2 from PyPI for any version of Python, included non installed versions.

1. Run the following command:
   `pip download --dest . --python-version 3.7 unicodedata2 --only-binary=:all: --platform=win32`
   - `--dest` indicates the destination directory.
   - `--only-binary=:all:` allows to download a binary (.whl), not the source.
2. Extract the content of the downloaded file as a zip and copy this content at the intended location, e.g. `charInfo\addon\globalPlugins\charinfo\UnicodeDataPKG\py37`.

