# Technical notes

## Update the Unicode data

Each time a new Unicode version is released, the data of this add-on needs to be updated to this release whenever possible.
The tasks required to update to a newer Unicode version is specific to each supported language.
For now only English and French are supported.
English is the base and the update of English data also updates the data that is not language aware such as matching a category or a block to a character.

## To update English data

English data is based on 2 sources:
* unicodedata2 package which is an up-to-date version of Python's unicodedata package; in the past, it was also backpported to Python 2 so in case of NVDA Python upgrade, one may expect such a backport again.
* Text files downloaded from Unicode website

## How to update unicodedata2 package?

To update unicodedata2 from PyPI for any version of Python, included non installed versions.

1. Run the following command in an empty directory:
   `pip download --dest . --python-version 3.7 unicodedata2 --only-binary=:all: --platform=win32`
   - `--dest` indicates the destination directory.
   - `--only-binary=:all:` allows to download a binary (.whl), not the source.
2. Extract the content of the downloaded file as a zip and copy this content at the intended location, i.e. today `charInfo\addon\globalPlugins\charinfo\UnicodeDataPKG\py37`.

## How to update text files from Unicode website

* Go to https://www.unicode.org/Public/UCD/latest/ucd/
* Download `Blocks.txt` and `PropertyValueAliases.txt`
* Paste these files in `charInfo\addon\globalPlugins\charinfo\locale\en`, overriding the older ones
