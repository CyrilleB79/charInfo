# Technical notes

## Update the Unicode data

Each time a new Unicode version is released, the data of this add-on needs to be updated to this release whenever possible.
The tasks required to update to a newer Unicode version is specific to each supported language.
For now only English and French are supported.
English is the base and the update of English data also updates the data that is not language aware such as matching a category or a block to a character.

### To update English data

English data is based on 2 sources:
* unicodedata2 package which is an up-to-date version of Python's unicodedata package; in the past, it was also backpported to Python 2 so in case of NVDA Python upgrade, one may expect such a backport again.
* Text files downloaded from Unicode website

#### How to update unicodedata2 package?

To update unicodedata2 from PyPI for any version of Python, included non installed versions.

1. Run the following command in an empty directory:
   `pip download --dest . --python-version 3.7 unicodedata2 --only-binary=:all: --platform=win32`
   - `--dest` indicates the destination directory.
   - `--only-binary=:all:` allows to download a binary (.whl), not the source.
2. Extract the content of the downloaded file as a zip and copy this content at the intended location, i.e. today `charInfo\addon\globalPlugins\charInfo\UnicodeDataPKG\py37`.

#### How to update text files from Unicode website

* Go to https://www.unicode.org/Public/UCD/latest/ucd/
* Download `Blocks.txt` and `PropertyValueAliases.txt`
* Paste these files in `charInfo\addon\globalPlugins\charInfo\locale\en`, overriding the older ones

### To update French data

* Download the latest following files found on http://hapax.qc.ca (and remove previous versions if any):
  * "Noms des blocs en français", e.g. [noms_blocs_v15.txt](http://hapax.qc.ca/noms_blocs_v15.txt)
  * "UnicodeData en français", e.g. [UnicodeData-5.0.0.fr.txt](http://hapax.qc.ca/UnicodeData-5.0.0.fr.txt)
* Rename the unicode data file (e.g. `UnicodeData-5.0.0.fr.txt`) to `UnicodeData.txt`
* If needed (probably very rarely), update `PropertyValueAliases.txt` according to http://hapax.qc.ca/UCD-4.0.0.fr.html; only the General categories (gc) are needed.

The French data will then be updated when compiling the add-on with scons.

Note: `UnicodeData-5.0.0.fr.txt` is very old.
It would be worth to compile newer unicode data from "[Liste des noms Unicode 15.0 et ISO/CEI 10646:2020 annotés](http://hapax.qc.ca/ListeNoms-15.0.0.txt)" (still to do).

### To add unicode data for another language

If you have a source containing unicode data for a language that is not yet supported, please contact the add-on author.
