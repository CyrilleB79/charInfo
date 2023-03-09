# A tool script for NVDA add-on Character information
# This script is used to generate and format the French (fr) Unicode data.
# Copyright (C) 2023 Cyrille Bougot
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

import os
import re

RE_SRC_BLOCK_LINE = re.compile('^[^;]*; *(?P<name>[^;]+?) *; *(?P<locName>[^;]+?) *$')
RE_EN_BLOCK_LINE = re.compile('^(?P<preMatch>[0-9A-F.]+; *)(?P<name>[^;]+?) *$')

addonPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
localeDataPath = os.path.join(addonPath, 'addon', 'globalPlugins', 'charinfo', 'locale')
frDataPath = os.path.join(localeDataPath, 'fr')
enDataPath = os.path.join(localeDataPath, 'en')
blockFile = os.path.join(frDataPath, 'Blocks.txt')

BLOCKS_FR_FILE_HEADER = \
	"""# Introduction note
	# 
	# This file is a French translation of https://unicode.org/Public/UNIDATA/Blocks.txt
	# It has been generated automatically thanks to the translations available in
	# http://hapax.qc.ca/{nomsBlocksFrFileName}
	#
	# End of introduction note
	
	"""


def getBlockTranslation(transFile):
	dic = {}
	with open(transFile, 'r', encoding='utf-8-sig') as f:
		for line in f:
			m = RE_SRC_BLOCK_LINE.match(line)
			if not m:
				raise LookupError(f'Unexpected line format: {line}')
			name = m['name']
			locName = m['locName']
			if name == 'C0 Controls and Basic Latin (Basic Latin)' and locName == 'Commandes C0 et latin de base (Latin de base)':
				name = 'Basic Latin'
				locName = 'Latin de base'
			elif name == 'C1 Controls and Latin-1 Supplement (Latin-1 Supplement)' and locName == 'Commandes C1 et supplément Latin-1 (Supplément Latin-1)':
				name = 'Latin-1 Supplement'
				locName = 'Supplément Latin-1'
			try:
				# Check if localized name in dictionary
				locNameInDic = dic[name]
			except KeyError:
				# Add localized name in dictionary
				dic[name] = locName
			else:
				# Check that localized name in the dic is the same as the one parsed on the current line.
				if locNameInDic != locName:
					raise ValueError(f'locNameInDic != locName - {locNameInDic} != {locName}')
	return dic
	
	
def generateBlockFile(src, dst, transFile):
	"""Generate a localized version of the file Blocks.txt on the same format as the English block file but with
	localized block names.
	
	@param src: the path of the English file Blocks.txt.
	 @param dst: the path of the translated file Blocks.txt to be generated.
	 @param transFile: the file containing the translation of the block names.
	"""
	
	p, transBlockFileName = os.path.split(transFile)
	trans = getBlockTranslation(transFile)
	with open(src, 'r', encoding='utf8') as fSrc:
		with open(dst, 'w', encoding='utf8') as fDst:
			fDst.write(BLOCKS_FR_FILE_HEADER.format(nomsBlocksFrFileName=transBlockFileName))
			for no, line in enumerate(fSrc):
				line = line.strip()
				if line == '' or line.startswith('#'):
					pass  # Do nothing
				else:
					m = RE_EN_BLOCK_LINE.match(line)
					if not m:
						raise LookupError(f'Match not found in line {no}: {line}')
					preMatch = m['preMatch']
					name = m['name']
					locName = trans[name]
					line = f'{preMatch}{locName}'
				fDst.write(line + '\n')
