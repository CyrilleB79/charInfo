# -*- coding: UTF-8 -*-

"""Script example generate symbol files from unicode data taking advantage of charInfo add-on.

This script generates the symbol file
- for characters from 1000 to 2000
- using fr_FR character names
- removing "lettre majuscule cyrillique" (or equivalent) from the name of the character

To run this script, copy/paste it in the Python console of NVDA.

This script is just a snippet that you can adapt for your needs (e.g. other languages, other character range,
etc.)
"""

from globalPlugins.charinfo import unicodeInfo

OUTPUT_FILE = r'h:\charlist.txt'


def generateCharList():
	def getNom(i):
		try:
			n = unicodeInfo.unicodeData['fr_FR'][i][0].lower()
			n = n.replace('lettre majuscule cyrillique', '')
			n = n.replace('lettre minuscule cyrillique', '')
			return n
		except KeyError:
			return 'NotAvailable'
	g = (chr(i) + '\t' + getNom(i) + '\tnone\tnever' for i in range(1000, 2000))
	with open(OUTPUT_FILE, 'w', encoding='utf8') as f:
		f.write('\n'.join(g))


generateCharList()
