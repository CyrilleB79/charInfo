# -*- coding: UTF-8 -*-
# NVDA add-on: Character information
# Copyright (C) 2019-2023 Cyrille Bougot
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

import globalPluginHandler
import addonHandler
import scriptHandler
import treeInterceptorHandler
import ui
from globalCommands import SCRCAT_SYSTEMCARET, commands, GlobalCommands
import api
import speech
import languageHandler
import textInfos
import controlTypes
import inputCore
from logHandler import log
from characterProcessing import (
	LocaleDataMap,
	CharacterDescriptions,
	SpeechSymbols,
	getCharacterDescription,
	SPEECH_SYMBOL_LEVEL_LABELS,
	SPEECH_SYMBOL_PRESERVE_LABELS,
	_localeSpeechSymbolProcessors,
)
import globalVars
import config
from utils import security

# Temporarily import private function as advised by Sean Budd from NVAccess.
# A public API can be requested by add-on developers 2-3 month after 2022.3.3 release if no issue is found.
from winAPI.sessionTracking import _isLockScreenModeActive

import sys
import os
import re
from enum import Enum
from functools import lru_cache


addonPath = os.path.dirname(__file__)


def getUniDatData():
	"""Import unicodedata2 (Unicodedata backport for python 2/3 updated to the latest unicode version)
	Note that if version of UnicodeData2 for the current version of Python cannot be founnd
	an exception is raised."""
	MAJORPYTHONVER = sys.version_info.major
	MINORPYTHONVER = sys.version_info.minor
	uniDataPath = os.path.join(
		addonPath,
		"UnicodeDataPKG",
		"py{0}{1}".format(MAJORPYTHONVER, MINORPYTHONVER)
	)
	if os.path.isdir(uniDataPath):
		sys.path.append(uniDataPath)
		import unicodedata2
		del sys.path[-1]
		return unicodedata2
	else:
		raise RuntimeError("No unicode data for Python version {0}.{1}".format(MAJORPYTHONVER, MINORPYTHONVER))


unicodedata = getUniDatData()

# Save NVDA translation function before overriding by add-on translation function.
nvdaTranslations = _

addonHandler.initTranslation()


UC_PRIVATE_USE_OFFSET = 0xf000
lstMsCharsets = ['Symbol',
	'Webdings',
	'Wingdings',
	'Wingdings 2',
	'Wingdings 3']

# Translators: Title on the char info displayed message
pageTitle = _("Detailed character information")
DATA_DIR = os.path.join(addonPath, "locale")
MSCHAR_DIR = os.path.join(addonPath, "mscharsets")
BLOCK_FILE = "Blocks.txt"
UNICODEDATA_FILE = "UnicodeData.txt"
PROP_VAL_ALIAS_FILE = "PropertyValueAliases.txt"


class InfoNotFoundError(LookupError):

	def __init__(self, message):
		self._message = message
	
	@property
	def message(self):
		return self._message


class NoFileError(InfoNotFoundError): pass


class NoValueError(InfoNotFoundError): pass


STR_NO_CHAR_ERROR = '?'
# Translators: Reported in the tables when no value is defined for a property of a specific character.
STR_VALUE_NOT_DEFINED = _('[Not defined]')
# Translators: Reported in the symbol and character description tables when no file corresponding to the row exists.
STR_NO_EXISTING_FILE = _('[No file]')


def removeAccelerator(s):
	"""Remove the '&' in a GUI string.
	Double ampersand is converted to simple ampersand.
	"""
	previousAmp = False
	out = ''
	for c in s:
		if previousAmp:
			out += c
			previousAmp = False
		elif c == '&':
			previousAmp = True
		else:
			out += c
	if previousAmp:
		out += c
	return out


def mkhi(itemType, content, attribDic={}):
	"""Creates an HTML item."""
	sAttribs = ''.join(f' {n}={v}' for n, v in attribDic.items())
	return f'<{itemType}{sAttribs}>{content}</{itemType}>'


css = """
td{
border : 1px solid black;
padding: 10px 15px;
}
table{
border-collapse: collapse;
}
""".replace('{', '{{').replace('}', '}}')


class UnicodeAttribute(Enum):
	CHARACTER = 'Character'
	NAME = 'Name'
	CLDR = 'CLDR'
	DECIMAL_VALUE = 'DecimalValue'
	HEX_VALUE = 'HexValue'
	CATEGORY = 'Category'
	BLOCK = 'Block'


# Mapping between UnicodeAttribute and a 2-tuple containing the attribute's translatable name and a function to retrieve the value.
unicodeAttributeMapping = {
	# Translators: A character attribute type in the Unicode table of the char info displayed message
	UnicodeAttribute.CHARACTER: (_("Character"), 'getCharStr'),
	# Translators: A character attribute type in the Unicode table of the char info displayed message
	UnicodeAttribute.NAME: (_("Name"), 'getNameStr'),
	# Translators: A character attribute type in the Unicode table of the char info displayed message
	UnicodeAttribute.CLDR: (_("CLDR name"), 'getCldrNameStr'),
	# Translators: A character attribute type in the Unicode table of the char info displayed message
	UnicodeAttribute.DECIMAL_VALUE: (_("Decimal value"), 'getDecStr'),
	# Translators: A character attribute type in the Unicode table of the char info displayed message
	UnicodeAttribute.HEX_VALUE: (_("Hex value"), 'getHexStr'),
	# Translators: A character attribute type in the Unicode table of the char info displayed message
	UnicodeAttribute.CATEGORY: (_("Category"), 'getCategoryStr'),
	# Translators: A character attribute type in the Unicode table of the char info displayed message
	UnicodeAttribute.BLOCK: (_("Block"), 'getBlockStr'),
}


class MsFontAttribute(Enum):
	NAME = "MsName"
	FONT = "MsFont"
	EQ_UNICODE_NAME = "EquivalentUnicodeCharacterName"
	EQ_UNICODE_HEX_VALUE = "EquivalentUnicodeCharacterHexValue"
	EQ_UNICODE_DECIMAL_VALUE = "EquivalentUnicodeCharacterDecimalValue"
	

msFontAttributeMapping = {
	# Translators: A character attribute type in the MS font table of the char info displayed message
	MsFontAttribute.NAME: (_("MS name"), 'getMsNameStr'),
	# Translators: A character attribute type in the MS font table of the char info displayed message
	MsFontAttribute.FONT: (_("MS Font"), 'getMsFontStr'),
	# Translators: A character attribute type in the MS font table of the char info displayed message
	MsFontAttribute.EQ_UNICODE_NAME: (_("Equivalent Unicode character name"), 'getUCEqNameStr'),
	# Translators: A character attribute type in the MS font table of the char info displayed message
	MsFontAttribute.EQ_UNICODE_HEX_VALUE: (_("Equivalent Unicode character hex value"), 'getUCEqHexValStr'),
	# Translators: A character attribute type in the MS font table of the char info displayed message
	MsFontAttribute.EQ_UNICODE_DECIMAL_VALUE: (_("Equivalent Unicode character decimal value"), 'getUCEqDecValStr'),
}


class NVDASymbolAttribute(Enum):
	REPORTED = "Reported"
	USER = "User"
	LOCALE = "Locale"
	LOCALE_CLDR = "LocaleCLDR"
	ENGLISH = "English"
	ENGLISH_CLDR = "EnglishCLDR"


nvdaSymbolAttributeMapping = {
	NVDASymbolAttribute.REPORTED: (
		# Translators: A character attribute type in the table on the char info displayed message
		_("Symbol description"),
		'getSymbolStr',
	),
	NVDASymbolAttribute.USER: (
		# Translators: A character attribute type in the table on the char info displayed message
		_("Symbol description in user file ({lang})"),
		'getSymbolUserStr',
	),
	NVDASymbolAttribute.LOCALE: (
		_("Symbol description in locale file{langInfo}"),
		'getSymbolLocaleStr'
	),
	NVDASymbolAttribute.LOCALE_CLDR: (
		# Translators: A character attribute type in the table on the char info displayed message
		_("Symbol description in locale CLDR file{langInfo}"),
		'getSymbolLocaleCLDRStr',
	),
	NVDASymbolAttribute.ENGLISH: (
		# Translators: A character attribute type in the table on the char info displayed message
		_("Symbol description in English file"),
		'getSymbolEnglishStr'
	),
	NVDASymbolAttribute.ENGLISH_CLDR: (
		# Translators: A character attribute type in the table on the char info displayed message
		_("Symbol description in English CLDR file"),
		'getSymbolEnglishCLDRStr',
	),
}


class NVDACharacterDescriptionAttribute(Enum):
	REPORTED = "Reported"
	LOCALE = "Locale"
	ENGLISH = "English"


nvdaCharacterDescriptionAttributeMapping = {
	# Translators: A character attribute type in the table on the char info displayed message
	NVDACharacterDescriptionAttribute.REPORTED: (_("Character description"), 'getCharacterDescriptionStr'),
	# Translators: A character attribute type in the table on the char info displayed message
	NVDACharacterDescriptionAttribute.LOCALE: (_("Character description{langInfo}"), 'getCharacterDescriptionLocaleStr'),
	# Translators: A character attribute type in the table on the char info displayed message
	NVDACharacterDescriptionAttribute.ENGLISH: (_("Character description (English file)"), 'getCharacterDescriptionEnglishStr'),
}


class Section(Enum):
	UNICODE = 'Unicode'
	MS_FONT = 'MSFont'
	NVDA_SYMBOL_DESC = 'NVDASymbolDescription'
	NVDA_CHAR_DESC = 'NVDACharacterDescription'


# A mapping between sections and a 2-tuple containing the section translatable name and its attributes.
sectionMapping = {
	# Translators: A section name in the char info displayed message
	Section.UNICODE: (_('Unicode'), unicodeAttributeMapping),
	# Translators: A section name in the char info displayed message
	Section.MS_FONT: (_('Microsoft font'), msFontAttributeMapping),
	# Translators: A section name in the char info displayed message
	Section.NVDA_SYMBOL_DESC: (_('Symbol description in NVDA'), nvdaSymbolAttributeMapping),
	# Translators: A section name in the char info displayed message
	Section.NVDA_CHAR_DESC: (_('Character description in NVDA'), nvdaCharacterDescriptionAttributeMapping),
}


class UnicodeInfo(object):

	def __init__(self):
		super(UnicodeInfo, self).__init__()
		self.blocks = {}
		self.generalCategories = {}
		self.unicodeData = {}
		self.cldr = {}
		self.langs = []
	
	def initLanguage(self, lang):
		self.langs.append(lang)
		
		self.blocks[lang] = self.getBlockInfo(lang)
		self.generalCategories[lang] = self.getGeneralCategoryInfo(lang)
		if lang != 'en':
		#For english we use directly unicodedata lib -> no init.
			self.unicodeData[lang] = self.getUnicodeDataInfo(lang)
	
	def getUnicodeDataInfo(self, lang):
		filePath = os.path.join(DATA_DIR, lang, UNICODEDATA_FILE)
		rc = re.compile(r"^([0-9A-F]+);([-\w<> ,']+);(\w+);.*$", re.U)
		dicChar = {}
		try:
			with open(filePath, 'r', encoding='UTF-8-sig') as f:
				for l in (ll.strip() for ll in f):
					if (l.startswith('#')
					or len(l) == 0):
						continue
					m = rc.match(l)
					if not m: raise ValueError(l)
					dicChar[int(m.group(1), 16)] = m.group(2), m.group(3)
			return dicChar
		except IOError:
			if '_' in lang:
				langFallback = lang.split('_')[0]
				log.debug(f'No Unicode data file for {lang}; fallback to {langFallback}.')
				return self.getUnicodeDataInfo(langFallback)
			else:
				log.debug(f'No Unicode data file for {lang}.')
				return None
	
	def getBlockInfo(self, lang):
		filePath = os.path.join(DATA_DIR, lang, BLOCK_FILE)
		rc = re.compile(r"^([0-9A-F]+)\.\.([0-9A-F]+); ([-'’ \w]+)$", re.U)
		lBlocks = []
		try:
			with open(filePath, 'r', encoding='UTF-8') as f:
				for l in (ll.strip() for ll in f):
					if (l.startswith('#')
					or len(l) == 0):
						continue
					m = rc.match(l)
					if not m: raise ValueError(l)
					inf = int(m.group(1), 16)
					sup = int(m.group(2), 16)
					name = m.group(3)
					lBlocks.append( (inf, sup, name) )
			return lBlocks
		except IOError:
			if '_' in lang:
				langFallback = lang.split('_')[0]
				log.debug(f'No block data for {lang}; fallback to {langFallback}.')
				return self.getBlockInfo(langFallback)
			else:
				log.debug(f'No block data file for {lang}.')
				return None
	
	def getGeneralCategoryInfo(self, lang):
		filePath = os.path.join(DATA_DIR, lang, PROP_VAL_ALIAS_FILE)
		rc = re.compile(r"^(gc) *; *(\w+) *; *([-' \w]+) *(?:[#;].*)?$", re.U)
		
		dicData = {}
		try:
			with open(filePath, 'r', encoding='UTF-8') as f:
				for l in (ll.strip() for ll in f):
					if (l.startswith('#')
					or len(l) == 0):
						continue
					m = rc.match(l)
					if not m: continue
					dicName = m.group(1)
					abbr = m.group(2)
					fullname = m.group(3)
					dic = dicData.get(dicName, {})
					if abbr in dic:
						raise ValueError('Duplicate value in same dic: ' + abbr)
					dic[abbr] = fullname
					dicData[dicName] = dic
			return dicData['gc']
		except IOError:
			if '_' in lang:
				langFallback = lang.split('_')[0]
				log.debug(f'No category data for {lang}; fallback to {langFallback}.')
				return self.getGeneralCategoryInfo(langFallback)
			else:
				log.debug(f'No category dta for {lang}.')
				return None


#Create UnicodeInfo instance
unicodeInfo = UnicodeInfo()


class LocaleData:
	""" A class to fetch and store locale data (symbols or characters) from .dic files for all locales.
	"""
	
	def __init__(self):
		self.langMapping = {}
	
	def fetch(self, lang):
		data = self.getDataFromFile(lang)
		if data:
			self.langMapping[lang] = lang
			return data
		if '_' in lang:
			langFallback = lang.split('_')[0]
			data = self.fetch(langFallback)
			if data:
				self.langMapping[lang] = langFallback
			else:
				self.langMapping[lang] = None
			return data
		self.langMapping[lang] = None
		return None
	
	def getDataLangForLang(self, lang):
		try:
			return self.langMapping[lang]
		except KeyError:
			self.fetch(lang)
			return self.langMapping[lang]


class SymbolData(LocaleData):

	def __init__(self, filename):
		super().__init__()
		self.filename = filename
	
	@lru_cache(maxsize=32)
	def getDataFromFile(self, lang):
		data = SpeechSymbols()
		try:
			data.load(os.path.join("locale", lang, self.filename), allowComplexSymbols=False)
			return data
		except IOError:
			return None		
	
	
class CharacterData(LocaleData):

	@lru_cache(maxsize=32)
	def getDataFromFile(self, lang):
		try:
			data = CharacterDescriptions(lang)
			return data
		except LookupError:
			return None		


symbolData = SymbolData("symbols.dic")
cldrData = SymbolData("cldr.dic")
characterData = CharacterData()


class MsCharsetsInfo(dict):

	def __init__(self, *args, **kw):
		super(MsCharsetsInfo, self).__init__(*args, **kw)
		for cs in lstMsCharsets:
			try:
				self[cs] = self.getCharsetInfo(cs)
			except IOError:
				pass
	
	def getCharsetInfo(self, cs):
		cs = cs.lower()
		cs = cs.replace(' ', '-')
		csPath = os.path.join(MSCHAR_DIR, cs + '.txt')
		csInfo = {}
		with open(csPath, 'r', encoding='utf-8') as f:
			for line in f:
				msNum, msName, ucNum = line.strip().split('\t')
				if ucNum == 'None':
					ucNum = None
				else:
					ucNum = int(ucNum)
				csInfo[int(msNum)] = (msName, ucNum)
		return csInfo


#Initialize MsCharsetsInfoInstance
msCharsetsInfo = MsCharsetsInfo()


class Character(object):

	CHAR_DESC_LOCALE_DATA_MAP = LocaleDataMap(CharacterDescriptions)

	def __init__(self, num, text, lang, font=None):
		super(Character, self).__init__()
		self.num = num
		self.text = text
		self.lang = lang
		self.font = font
		if self.isMsFont():
			self.msCharInfo = msCharsetsInfo[self.font][self.num - UC_PRIVATE_USE_OFFSET]
			eqUCNum = self.msCharInfo[1]
			if eqUCNum is None:
				self.UCEqChar = None
			else:
				self.UCEqChar = Character(eqUCNum, chr(eqUCNum), self.lang)
	
	def getCharStr(self):
		return self.text
	
	def getNameStr(self):
		names = [self.getNameValue(l) for l in unicodeInfo.langs]
		return ' / '.join(n for n in names if n is not None)
	
	def getNameValue(self, lang):
		if lang == 'en':
			try:
				return unicodedata.name(self.text)
			except ValueError:
				return STR_NO_CHAR_ERROR
		if not unicodeInfo.unicodeData[lang]:
			return None
		try:
			return unicodeInfo.unicodeData[lang][self.num][0]
		except KeyError:
			return STR_NO_CHAR_ERROR
	
	def getCldrNameStr(self):
		names = [self.getCldrNameValue(l) for l in unicodeInfo.langs]
		return ' / '.join(n for n in names if n is not None)
	
	def getCldrNameValue(self, lang):
		data = cldrData.fetch(lang)
		if not data:
			return None
		try:
			return data.symbols[self.text].replacement
		except KeyError:
			return STR_NO_CHAR_ERROR
	
	def getDecStr(self):
		return str(self.num)
	
	def getHexStr(self):
		return hex(self.num)
	
	def getCategoryStr(self):
		cat = unicodedata.category(self.text)
		if cat == 'Cn':
			try:
				cat = unicodeInfo.unicodeData['en'][self.num][1]
			except KeyError:
				pass
		catNames = [self.getCategoryValue(cat, l) for l in unicodeInfo.langs]
		return cat + ' - ' + ' / '.join(c for c in catNames if c is not None)
	
	def getCategoryValue(self, cat, lang):
		if not unicodeInfo.generalCategories[lang]:
			return None
		return unicodeInfo.generalCategories[lang][cat]
	
	def getBlockStr(self):
		blockNames = [self.getBlockValue(l) for l in unicodeInfo.langs]
		return ' / '.join(b for b in blockNames if b is not None)
	
	def getBlockValue(self, lang):
		if unicodeInfo.blocks[lang] is None:
			return None
		for inf, sup, name in unicodeInfo.blocks[lang]:
			if inf <= self.num <= sup:
				return name
		if lang == "en":
			# Translators: Reported in the Unicode information table when the character does not belong to any block.
			return _("No Block")
		else:
			return None
	
	def getMsNameStr(self):
		return self.msCharInfo[0]
	
	def getMsFontStr(self):
		return self.font
	
	def getUCEqNameStr(self):
		if self.UCEqChar is None:
			return STR_NO_CHAR_ERROR
		names = [self.UCEqChar.getNameValue(l) for l in unicodeInfo.langs]
		return ' / '.join(n for n in names if n is not None)
	
	def getUCEqHexValStr(self):
		if self.UCEqChar is None:
			return STR_NO_CHAR_ERROR
		return hex(self.UCEqChar.num)
	
	def getUCEqDecValStr(self):
		if self.UCEqChar is None:
			return STR_NO_CHAR_ERROR
		return str(self.UCEqChar.num)
	
	def isMsFont(self):
		if self.font in lstMsCharsets and (
		self.num >= UC_PRIVATE_USE_OFFSET and self.num < UC_PRIVATE_USE_OFFSET + 256):
			return True
		else:
			return False
	
	def getCharacterDescriptionStr(self):
		desc = getCharacterDescription(self.lang, self.text.lower())
		if desc is None:
			return STR_VALUE_NOT_DEFINED
		IDEOGRAPHIC_COMMA = "\u3001"
		return IDEOGRAPHIC_COMMA.join(desc)
	
	def getCharacterDescriptionLocaleStr(self, lang=None):
		if not lang:
			lang = self.lang
		try:
			localData = self.CHAR_DESC_LOCALE_DATA_MAP.fetchLocaleData(lang)
		except LookupError:
			return STR_NO_EXISTING_FILE
		desc = localData.getCharacterDescription(self.text.lower())
		if not desc:
			return STR_VALUE_NOT_DEFINED
		IDEOGRAPHIC_COMMA = "\u3001"
		return IDEOGRAPHIC_COMMA.join(desc)
	
	def getCharacterDescriptionEnglishStr(self):
		return self.getCharacterDescriptionLocaleStr(lang="en")	
	
	def getSymbolStr(self, locale=None):
		if not locale:
			locale = self.lang
		try:
			ss = _localeSpeechSymbolProcessors.fetchLocaleData(locale)
		except LookupError:
			if not locale.startswith("en_"):
				return self.getSymbolStr("en")
			raise RuntimeError(f'Unexpected error. [locale={locale}]')
		try:
			info = ss.computedSymbols[self.text]
		except KeyError:
			return (STR_VALUE_NOT_DEFINED, ) * 3
		return (
			info.replacement,
			SPEECH_SYMBOL_LEVEL_LABELS.get(info.level, STR_VALUE_NOT_DEFINED),
			SPEECH_SYMBOL_PRESERVE_LABELS.get(info.preserve, STR_VALUE_NOT_DEFINED),
		)	
	
	def getSymbolUserStr(self):
		locale = self.lang.split('_')[0]
		try:
			info = self.getSymbolInfo(os.path.join(globalVars.appArgs.configPath, f"symbols-{locale}.dic"), allowComplexSymbols=False)
			return (
				info.replacement,
				SPEECH_SYMBOL_LEVEL_LABELS.get(info.level, STR_VALUE_NOT_DEFINED),
				SPEECH_SYMBOL_PRESERVE_LABELS.get(info.preserve, STR_VALUE_NOT_DEFINED),
			)
		except NoValueError:
			return (STR_VALUE_NOT_DEFINED, ) * 3
		except NoFileError:
			return STR_NO_EXISTING_FILE
	
	def getSymbolLocaleStr(self, locale=None, cldr=False):
		if not locale:
			locale = self.lang
		if cldr:
			data = cldrData.fetch(locale)
		else:
			data = symbolData.fetch(locale)
		if not data:
			return STR_NO_EXISTING_FILE
		try:
			symb = data.symbols[self.text]
		except KeyError:
			return (STR_VALUE_NOT_DEFINED, ) * 3
		return (
			symb.replacement,
			SPEECH_SYMBOL_LEVEL_LABELS.get(symb.level, STR_VALUE_NOT_DEFINED),
			SPEECH_SYMBOL_PRESERVE_LABELS.get(symb.preserve, STR_VALUE_NOT_DEFINED),
		)
	
	def getSymbolLocaleCLDRStr(self, locale=None):
		return self.getSymbolLocaleStr(locale, cldr=True)
	
	def getSymbolEnglishStr(self, cldr=False):\
		return self.getSymbolLocaleStr(locale='en', cldr=cldr)
	
	def getSymbolEnglishCLDRStr(self):
		return self.getSymbolEnglishStr(cldr=True)
	
	def getSymbolInfo(self, filepath, allowComplexSymbols=True):
		symbols = SpeechSymbols()
		try:
			symbols.load(filepath, allowComplexSymbols=allowComplexSymbols)
		except IOError:
			raise NoFileError(filepath)
		try:
			return symbols.symbols[self.text]
		except KeyError:
			raise NoValueError(self.text)


def convertToOnOff(val: bool) -> str:
	if val is True:
		# Translators: The value of an option reported in symbol description section of the character info repot.
		return _("On")
	if val is False:
		# Translators: The value of an option reported in symbol description section of the character info repot.
		return _("Off")
	raise ValueError(f'Unexpected value: {val}')


class Characters(object):

	def __init__(self, text, lang, font):
		self.charList = [Character(ord(c), c, lang=lang, font=font) for c in text]
		self.lang = lang
		self.font = font		
	
	def createHtmlInfoMessage(self, text):
		doctype = '<!doctype html>'
		head = mkhi('head', '<meta charset= "utf-8"/>' + mkhi('style', css))
		content = []
		title = mkhi('h1', text)
		content.append(title)
		validSectionList = [s for s in Section]
		# Keep MSFont section only for MS characters.
		if all([not c.isMsFont() for c in self.charList]):
			validSectionList.remove(Section.MS_FONT)
		for section in validSectionList:
			htmlSection = self.createHtmlInfoSection(section)
			content.append(htmlSection)
		body = mkhi(
			'body',
			''.join(content),
		)
		return mkhi(
			'html',
			doctype + head + body,
		)
	
	def createHtmlInfoSection(self, section):
			content = []
			name, mapping = sectionMapping[section]
			title = mkhi('h2', name)
			content.append(title)
			table = self.createHtmlInfoTable(section)
			content.append(table)
			if section == Section.NVDA_SYMBOL_DESC:
				footNotes = self.createHtmlSymbolInfoFootNote()
				content.append(footNotes)
			return ''.join(content)
	
	def createHtmlInfoTable(self, section):
		"""Create the HTML string corresponding to the table displaying names and values of various character attributes.
		"""
		
		content = []
		if section == Section.NVDA_SYMBOL_DESC:
			header = self.createHtmlInfoHeaderForSymbolDesc()
		else:
			header = self.createHtmlInfoHeader()
		content.append(header)
		name, mapping = sectionMapping[section]
		# Locally copy the mapping to modify it
		mapping = dict(mapping)
		toRemove = set()
		if self.lang.split('_')[0] == "en":
			toRemove.update({NVDASymbolAttribute.LOCALE, NVDASymbolAttribute.LOCALE_CLDR, NVDACharacterDescriptionAttribute.LOCALE})
		if not config.conf["speech"]["includeCLDR"]:
			toRemove.update({NVDASymbolAttribute.LOCALE_CLDR, NVDASymbolAttribute.ENGLISH_CLDR})
		for attr in toRemove:
			try:
				del mapping[attr]
			except KeyError:
				pass
		for key, (attr, getter) in mapping.items():
			if key == NVDASymbolAttribute.USER:
				attr = attr.format(lang=self.lang)
			elif key == NVDASymbolAttribute.LOCALE:
				lang = symbolData.getDataLangForLang(self.lang)
				if lang:
					langInfo = f' ({lang})'
				else:
					langInfo = ''
				attr = attr.format(langInfo=langInfo)
			elif key == NVDASymbolAttribute.LOCALE_CLDR:
				lang = cldrData.getDataLangForLang(self.lang)
				if lang:
					langInfo = f' ({lang})'
				else:
					langInfo = ''
				attr = attr.format(langInfo=langInfo)
			elif key == NVDACharacterDescriptionAttribute.LOCALE:
				lang = characterData.getDataLangForLang(self.lang)
				if lang:
					langInfo = f' ({lang})'
				else:
					langInfo = ''
				attr = attr.format(langInfo=langInfo)
			row = self.createHtmlInfoRow(
				attr,
				[getattr(c, getter)() for c in self.charList],
				section,
			)
			content.append(row)	
		return mkhi(
			'table',
			''.join(content),
			{'border':'1'}
		)
	
	def createHtmlInfoHeader(self):	
		nChars = len(self.charList)
		if nChars == 1:
			# Translators: A column header on the char info displayed message
			headerVal = _("Value")
		else:
			# Translators: A column title on the char info displayed message
			headerVal = _("Character {numChar}")
		
		htmlHeaderLabel = mkhi(
			'th',
			# Translators: A column title on the char info displayed message
			_("Attribute"),
			attribDic={'scope': 'row'},
		)
		htmlHeaderValues = ''.join(
			mkhi(
				'th',
				headerVal.format(numChar=n + 1),
				attribDic={'scope': 'col'},
			) for n in range(nChars)
		)
		return mkhi(
			'tr',
			htmlHeaderLabel + htmlHeaderValues,
		)
	
	def createHtmlInfoHeaderForSymbolDesc(self):
		nChars = len(self.charList)
		htmlHeaderLabel = mkhi(
			'th',
			# Translators: A column title on the char info displayed message
			_("Attribute"),
			attribDic={'scope': 'row'},
		)
		htmlHeaderValues = []
		for n in range(nChars):
			if nChars > 1:
				charIndicator = f' ({n + 1})'
			else:
				charIndicator = ''
			val = nvdaTranslations("Replacement") + charIndicator
			htmlHeaderValues.append(mkhi('th', val, attribDic={'scope': 'col'}))
			val = nvdaTranslations("Level") + charIndicator
			htmlHeaderValues.append(mkhi('th', val, attribDic={'scope': 'col'}))
			val = nvdaTranslations("Preserve") + charIndicator
			htmlHeaderValues.append(mkhi('th', val, attribDic={'scope': 'col'}))
		htmlHeaderRow = htmlHeaderLabel + ''.join(htmlHeaderValues)
		return mkhi(
				'tr',
				htmlHeaderRow,
		)
	
	def createHtmlInfoRow(self, attr, valueList, session):
		content = []
		htmlAttribute = mkhi('th', attr)
		content.append(htmlAttribute)
		for value in valueList:
			if session == Section.NVDA_SYMBOL_DESC:
				if isinstance(value, tuple):
					htmlCells = ''.join(mkhi('td', i) for i in value)
				else:
					htmlCells = mkhi('td', value, attribDic={'colspan': 3})
			else:
				htmlCells = mkhi('td', value)
			content.append(htmlCells)
		return mkhi('tr', ''.join(content))
	
	def createHtmlSymbolInfoFootNote(self):
		content = []
		introStr = _("Options used to compute the symbol:")
		content.append(mkhi('p', introStr))
		optionList = []
		optionList.append(
			'{txt}: {val}'.format(
				txt=removeAccelerator(
					nvdaTranslations("Include Unicode Consortium data (including emoji) when processing characters and symbols"),
				),
				val=convertToOnOff(config.conf["speech"]["includeCLDR"]),
			)
		)
		optionList.append(
			'{txt}: {val}'.format(
				txt=removeAccelerator(
					nvdaTranslations("Trust voice's language when processing characters and symbols"),
				),
				val=convertToOnOff(config.conf["speech"]["trustVoiceLanguage"]),
			)
		)
		useVoiceLanguage = config.conf["speech"]["trustVoiceLanguage"]
		if useVoiceLanguage:
			try:
				_localeSpeechSymbolProcessors.fetchLocaleData(self.lang)
				useNVDAInterfaceLanguage = False
			except LookupError:
				useNVDAInterfaceLanguage = True
		else:
			useNVDAInterfaceLanguage = True
		if useVoiceLanguage:
			optionList.append(
				'{txt}: {val}'.format(
					txt=_("Voice language"),
					val=self.lang,
				)
			)
		if useNVDAInterfaceLanguage:
			optionList.append(
				'{txt}: {val}'.format(
					txt=_("NVDA interface language"),
					val=languageHandler.getLanguage(),
				)
			)
		content.append(mkhi(
			'ul',
			''.join(mkhi('li', item) for item in optionList),
		))
		return ''.join(content)		


originalGetSafeScripts = security.getSafeScripts


def patchedGetSafeScripts():
	# Current running charInfo global plugin
	ci = next(gp for gp in globalPluginHandler.runningPlugins if gp.__module__ == 'globalPlugins.charinfo')
	safeScripts = originalGetSafeScripts()
	safeScripts.add(ci.script_review_currentCharacter)
	return safeScripts


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		log.debug('Unicode version: ' + unicodedata.unidata_version)
		self.initUnicodeInfo()
		biScript = GlobalCommands.script_review_currentCharacter
		self.biScriptDoc = biScript.__doc__
		biScriptInfo = inputCore.manager.getAllGestureMappings()[biScript.category][self.biScriptDoc]
		biScriptGestureMap = {g:biScriptInfo.scriptName for g in biScriptInfo.gestures}
		#Empty the original script's docstring to prevent it from being displayed in gesture setting window.
		commands.script_review_currentCharacter.__func__.__doc__ = ""
		#Delete all associated gestures to original script
		self.bindGestures(biScriptGestureMap)
		security.getSafeScripts = patchedGetSafeScripts
	
	def initUnicodeInfo(self):
		langUI = languageHandler.getLanguage()
		if langUI == 'en':
			langs = ['en']
		else:
			langs = ['en', langUI]
		for lang in langs:
			unicodeInfo.initLanguage(lang)
	
	def terminate (self):
		#Restore built-in script doc so that it be listed in the gesture modification dialog and supports help
		commands.script_review_currentCharacter.__func__.__doc__ = self.biScriptDoc
		#Clear charInfo plugin gestures
		self.clearGestureBindings()
		# Restore original getSafeScripts function
		security.getSafeScripts = originalGetSafeScripts
		super(GlobalPlugin, self).terminate ()
	
	def script_review_currentCharacter(self, gesture):
		scriptCount=scriptHandler.getLastScriptRepeatCount()
		if scriptCount >= 4:
			return
		elif scriptCount <= 2:
			commands.script_review_currentCharacter(gesture)
			return
		if _isLockScreenModeActive():
			# In lock screen do not display character info. The character information window would appear only
			# once the session is reopened, which is quite useless and confusing.
			return
		self.displayCurrentCharInfoMessage(info = api.getReviewPosition().copy())
	# Translators: A part of the message presented in input help mode.
	script_review_currentCharacter.__doc__ = commands.script_review_currentCharacter.__doc__ + _(". Pressing four times presents a message with detailed information on this character.")
	script_review_currentCharacter.category = commands.script_review_currentCharacter.category
	
	def script_currentCharInfo(self, gesture):
		self.displayCurrentCharInfoMessage(info = api.getReviewPosition().copy())
	# Translators: The message presented in input help mode.
	script_currentCharInfo.__doc__ = _("Presents a message with detailed information on the character of the current navigator object where the review cursor is situated.")
	script_currentCharInfo.category = commands.script_review_currentCharacter.category
	
	def script_currentCharAtCaretInfo(self, gesture):
		obj = api.getFocusObject()
		treeInterceptor = obj.treeInterceptor
		if isinstance(treeInterceptor, treeInterceptorHandler.DocumentTreeInterceptor) and not treeInterceptor.passThrough:
			obj = treeInterceptor
		try:
			info = obj.makeTextInfo(textInfos.POSITION_CARET)
		except (NotImplementedError, RuntimeError):
			# Translators: Reported when there is no caret
			ui.message(_("No caret"))
			return
		self.displayCurrentCharInfoMessage(info)
	# Translators: The message presented in input help mode.
	script_currentCharAtCaretInfo.__doc__ = _("Presents a message with detailed information on the character at the position of the caret.")
	script_currentCharAtCaretInfo.category = SCRCAT_SYSTEMCARET
	
	def displayCurrentCharInfoMessage(self, info):
		info.expand(textInfos.UNIT_CHARACTER)
		if info.text == '':
			try:
				reasonCaret = controlTypes.OutputReason.CARET  # NVDA 2021.1 and later
			except AttributeError:
				reasonCaret = controlTypes.REASON_CARET  # NVDA 2020.4 and older
			speech.speakTextInfo(info, unit=textInfos.UNIT_CHARACTER, reason=reasonCaret)
			return
		font = self.getCurrCharFontName(info)
		lang = None
		if config.conf['speech']['autoLanguageSwitching']:
			# Get language from text tagging if any
			lang = self.getCurrentLanguage(info)
		if not lang:
			# Get language from synth or UI depending on if trust voice language is activated
			# and if it is possible to know the language of the current synth.
			lang = speech.getCurrentLanguage()
		allChars = Characters(info.text, lang=lang, font=font)
		htmlMessage = allChars.createHtmlInfoMessage(info.text)
		ui.browseableMessage(htmlMessage, title=pageTitle, isHtml= True)
	
	def getCurrCharFontName(self, info):
		configDocFormatting = config.conf['documentFormatting'].items()
		formatConfig = {k:False for k, v in configDocFormatting}
		formatConfig['reportFontName'] = True
		info=info.copy()
		info.expand(textInfos.UNIT_CHARACTER)
		for field in info.getTextWithFields(formatConfig):
			if isinstance(field, textInfos.FieldCommand) and isinstance(field.field, textInfos.FormatField):
				try:
					return field.field["font-name"]
				except KeyError:
					return None
		return None
	
	def getCurrentLanguage(self, info):
		configDocFormatting = config.conf['documentFormatting'].items()
		formatConfig = {k:False for k, v in configDocFormatting}
		info=info.copy()
		info.expand(textInfos.UNIT_CHARACTER)
		for field in info.getTextWithFields(formatConfig):
			if isinstance(field, textInfos.FieldCommand) and isinstance(field.field, textInfos.FormatField):
				try:
					return field.field["language"]
				except KeyError:
					pass
		return None
