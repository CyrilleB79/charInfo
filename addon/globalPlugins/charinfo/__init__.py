# -*- coding: UTF-8 -*-
#globalPlugins/charinfo/__init__.py
#NVDA add-on: Character information
#Copyright (C) 2019 Cyrille Bougot
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

from __future__ import unicode_literals

import globalPluginHandler
import scriptHandler
import ui
from globalCommands import SCRCAT_TEXTREVIEW, commands, GlobalCommands
import api
import speech
import languageHandler
import textInfos
import controlTypes
import inputCore
from logHandler import log
from characterProcessing import SpeechSymbols
import config

import os
import re
import sys
from codecs import open

#Use unicodedata2 (Unicodedata backport for python 2/3 updated to the latest unicode version)
if sys.version_info.major == 2: #Python2
	addonPath = os.path.dirname(__file__).decode("mbcs")
	sys.path.append(os.path.join(addonPath, "libPy2"))
else: #Python3
	addonPath = os.path.dirname(__file__)
	sys.path.append(os.path.join(addonPath, "libPy3"))
import unicodedata2 as unicodedata
del sys.path[-1]

	
import addonHandler

addonHandler.initTranslation()

UC_PRIVATE_USE_OFFSET = 0xf000
lstMsCharsets = ['Symbol', 
	'Webdings',
	'Wingdings',
	'Wingdings 2',
	'Wingdings 3']

# Translators: Title on the char info displayed message
pageTitle = _("Detailed character information'")
DATA_DIR = os.path.join(addonPath, "locale")
MSCHAR_DIR = os.path.join(addonPath, "mscharsets")
BLOCK_FILE = "Blocks.txt"
UNICODEDATA_FILE = "UnicodeData.txt"
PROP_VAL_ALIAS_FILE = "PropertyValueAliases.txt"

STR_NO_CHAR_ERROR = '?'
#STR_NO_CHAR_ERROR = 'N/A No char'
STR_NO_FILE_ERROR = '?'
#STR_NO_FILE_ERROR = 'N/A No file'

def mkhi(itemType, content, attribDic={}):
	"""Creates an HTML item."""
	sAttribs = ''.join(' ' + n + '=' + v for n,v in attribDic.items())
	return '<' + itemType + sAttribs + '>' + content + '</' + itemType + '>'
	
def createHtmlInfoTable(infoList):
	"""Create the HTML string corresponding to the table displaying names and values of various character attributes.
	Parameters:
	infoList: a 2-tuple list in which each (attribute, value) tuple correspond to a line in the table.
	"""
	tdAttr = {}
	items = (mkhi('td', l, tdAttr) + mkhi('td', v, tdAttr) for l,v in infoList)
	# Translators: A column title on the char info displayed message
	titleLabel = _("Attribute")
	# Translators: A column title on the char info displayed message
	titleVal = _("Value")
	return mkhi(
		'table',
		mkhi('tr', mkhi('th', titleLabel) + mkhi('th', titleVal)) +
		''.join(mkhi('tr', i) for i in items),
		{'border':'1'})

css = """
td{
border : 1px solid black;
padding: 10px 15px;
}
table{
border-collapse: collapse;
}
""".replace('{','{{').replace('}','}}')

#The HTML message page code
gHtmlMessage = '<!doctype html>' + \
	mkhi('html',
	mkhi('head', '<meta charset= "utf-8"/>' + mkhi('style', css)) + 
	mkhi('body',
	mkhi('h1', pageTitle)
	+ '{infoTable}'))
	

requiredInfoList = [
	# Translators: A character attribute type in the table on the char info displayed message
	(_("Character"), 'getCharStr'),
	# Translators: A character attribute type in the table on the char info displayed message
	(_("Name"), 'getNameStr'),
	# Translators: A character attribute type in the table on the char info displayed message
	(_("CLDR name"), 'getCldrNameStr'),
	# Translators: A character attribute type in the table on the char info displayed message
	(_("Decimal value"), 'getDecStr'),
	# Translators: A character attribute type in the table on the char info displayed message
	(_("Hex value"), 'getHexStr'),
	# Translators: A character attribute type in the table on the char info displayed message
	(_("Category"), 'getCategoryStr'),
	# Translators: A character attribute type in the table on the char info displayed message
	(_("Block"), 'getBlockStr'),
	]
	
msCharInfoList = [
	# Translators: A character attribute type in the table on the char info displayed message
	(_("MS name"), 'getMsNameStr'),
	# Translators: A character attribute type in the table on the char info displayed message
	(_("MS Font"), 'getMsFontStr'),
	# Translators: A character attribute type in the table on the char info displayed message
	(_("Equivalent Unicode character name"), 'getUCEqNameStr'),
	# Translators: A character attribute type in the table on the char info displayed message
	(_("Equivalent Unicode character hex value"), 'getUCEqHexValStr'),
	# Translators: A character attribute type in the table on the char info displayed message
	(_("Equivalent Unicode character decimal value"), 'getUCEqDecValStr'),
	]

if sys.version_info.major >= 3: #Python3
	unichr = chr

def unichr32(v):
	try:
		return unichr(v)
	except ValueError:
		s = "\\U%08x" % v
		text = s.decode('unicode-escape')
		return text
		
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
		self.cldr[lang] = self.getCldrInfo(lang)
		
	@staticmethod
	def getUnicodeDataInfo(lang):
		filePath = os.path.join(DATA_DIR, lang, UNICODEDATA_FILE)
		rc = re.compile(r"^([0-9A-F]+);([-\w<> ,']+);(\w+);.*$", re.U)
		dicChar = {}
		try:
			with open(filePath, 'r', encoding='UTF-8') as f:
				for l in (ll.strip() for ll in f):
					if (l.startswith('#')
					or len(l) == 0):
						continue
					m = rc.match(l)
					if not m: raise ValueError(l)
					dicChar[int(m.group(1), 16)] = m.group(2), m.group(3)
			return dicChar
		except IOError:
			return None
			
		
	
	@staticmethod
	def getCldrInfo(lang):
		cldrInfo = SpeechSymbols()
		try:
			cldrInfo.load(os.path.join("locale", lang, "cldr.dic"), allowComplexSymbols=False)
			return cldrInfo
		except IOError:
			return None
		
	@staticmethod
	def getBlockInfo(lang):
		filePath = os.path.join(DATA_DIR, lang, BLOCK_FILE)
		rc = re.compile(r"^([0-9A-F]+)\.\.([0-9A-F]+); ([-' \w]+)$", re.U)
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
			return None
		
	@staticmethod
	def getGeneralCategoryInfo(lang):
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
			return None

#Create UnicodeInfo instance
unicodeInfo = UnicodeInfo()

class MsCharsetsInfo(dict):
	def __init__(self, *args, **kw):
		super(MsCharsetsInfo, self).__init__(*args, **kw)
		for cs in lstMsCharsets:
			try:
				self[cs] = self.getCharsetInfo(cs)
			except IOError:
				pass
		
	def getCharsetInfo(self,cs):
		cs = cs.lower()
		cs = cs.replace(' ', '-')
		csPath = os.path.join(MSCHAR_DIR, cs + '.txt')
		csInfo = {}
		with open(csPath, 'r', encoding='utf-8') as f:
			for line in f:
				msNum,msName,ucNum = line.strip().split('\t')
				if ucNum == 'None':
					ucNum = None
				else:
					ucNum = int(ucNum)
				csInfo[int(msNum)] = (msName, ucNum)
		return csInfo
		
		
#Initialize MsCharsetsInfoInstance
msCharsetsInfo = MsCharsetsInfo()

class Character(object):

	def __init__(self, cNum, cText, cFont=None):
		super(Character, self).__init__()
		self.num = cNum
		self.text = cText
		if self.num >= 0x10000:
		#For NVDA < 2019.1 that does not support 32-bit char
			s = "\\U%08x" % self.num
			try: #Python2
				self.text = s.decode('unicode-escape')
			except AttributeError: #Python3 #Python3
				pass #NVDA python 3 so NVDA > 2019.1, so 32-bit characters are handled correctly
		self.font = cFont
		if self.isMsFont():
			self.msCharInfo = msCharsetsInfo[self.font][self.num - UC_PRIVATE_USE_OFFSET]
			msText = self.msCharInfo[1]
			if msText is None:
				self.UCEqChar = None
			else:
				self.UCEqChar = Character(msText, unichr32(msText))
		
	def getCharStr(self):
		return self.text
	def getNameStr(self):
		names = [self.getNameValue(l) for l in unicodeInfo.langs]
		return ' / '.join(names)
		
	def getNameValue(self, lang):
		if lang == 'en':
			try:
				return unicodedata.name(self.text)
			except ValueError:
				return STR_NO_CHAR_ERROR
		if not unicodeInfo.unicodeData[lang]:
			return STR_NO_FILE_ERROR
		try:
			return unicodeInfo.unicodeData[lang][self.num][0]
		except KeyError:
			return STR_NO_CHAR_ERROR
	
	def getCldrNameStr(self):
		names = [self.getCldrNameValue(l) for l in unicodeInfo.langs]
		return ' / '.join(names)
		
	def getCldrNameValue(self, lang):
		if not unicodeInfo.cldr[lang]:
			return STR_NO_FILE_ERROR
		try:
			return unicodeInfo.cldr[lang].symbols[self.text].replacement
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
		return cat + ' - ' + ' / '.join(catNames)
		
	def getCategoryValue(self, cat, lang):
		if not unicodeInfo.generalCategories[lang]:
			return STR_NO_FILE_ERROR
		return unicodeInfo.generalCategories[lang][cat]
		
	def getBlockStr(self):
		blockNames = [self.getBlockValue(l) for l in unicodeInfo.langs]
		return ' / '.join(blockNames)
		
	def getBlockValue(self, lang):
		if unicodeInfo.blocks[lang] is None:
			return STR_NO_FILE_ERROR
		for inf,sup,name in unicodeInfo.blocks[lang]:
			if inf <= self.num <= sup:
				return name
		return STR_NO_CHAR_ERROR
	
	def getMsNameStr(self):
		return self.msCharInfo[0]
		
	def getMsFontStr(self):
		return self.font
		
	def getUCEqNameStr(self):
		if self.UCEqChar is None:
			return STR_NO_CHAR_ERROR
		names = [self.UCEqChar.getNameValue(l) for l in unicodeInfo.langs]
		return ' / '.join(names)
		
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
		commands.script_review_currentCharacter.__dict__['__doc__'] = ""
		#Delete all associated gestures to original script
		self.bindGestures(biScriptGestureMap)
		
	def initUnicodeInfo(self):
		langUI = languageHandler.getLanguage().split('_')[0]
		if langUI == 'en':
			langs = ['en']
		else:
			langs = ['en', langUI]
		for lang in langs:
			unicodeInfo.initLanguage(lang)
	
	def terminate (self):
		#Restore built-in script doc so that it be listed in the gesture modification dialog and supports help
		commands.script_review_currentCharacter.__dict__['__doc__'] = self.biScriptDoc
		#Clear charInfo plugin gestures
		self.clearGestureBindings()
		super(GlobalPlugin, self).terminate ()
		
	def script_review_currentCharacter(self,gesture):
		scriptCount=scriptHandler.getLastScriptRepeatCount()
		if scriptCount >= 4:
			return
		elif scriptCount <= 2:
			commands.script_review_currentCharacter(gesture)
			return
		self.displayCurrentCharInfoMessage()
	# Translators: A part of the message presented in input help mode.
	script_review_currentCharacter.__doc__ = commands.script_review_currentCharacter.__doc__ + _(". Pressing four times presents a message with detailed information on this character.")
	script_review_currentCharacter.category = commands.script_review_currentCharacter.category
	
	def script_currentCharInfo(self, gesture):
		self.displayCurrentCharInfoMessage()
	# Translators: The message presented in input help mode.
	script_currentCharInfo.__doc__ = _("Presents a message with detailed information on the character of the current navigator object where the review cursor is situated.")
	script_currentCharInfo.category = commands.script_review_currentCharacter.category
		
	def displayCurrentCharInfoMessage(self):
		### Code inspired from NVDA script_review_currentCharacter in file globalCommands.py
		info=api.getReviewPosition().copy()
		info.expand(textInfos.UNIT_CHARACTER)
		if info.text == '':
			speech.speakTextInfo(info,unit=textInfos.UNIT_CHARACTER,reason=controlTypes.REASON_CARET)
			return
		font = self.getCurrCharFontName(info)
		try:
			c = ord(info.text)
		except TypeError:
			# This might be a character taking multiple code points.
			# If it is a 32 bit character, encode it to UTF-32 and calculate the ord manually.
			# In Python 3, this is no longer necessary.
			try:
				encoded = info.text.encode("utf_32_le")
			except UnicodeEncodeError:
				c = None
			else:
				if len(encoded)==4:
					c = sum(ord(cp)<<i*8 for i, cp in enumerate(encoded))
				else:
					c = None
		### End code copy
		
		if c is not None:
			char = Character(c, info.text, font)
			computedInfoList = [(t, getattr(char, f)()) for t,f in requiredInfoList]
			if char.isMsFont():
				computedInfoList.extend([(t, getattr(char, f)()) for t,f in msCharInfoList])
		else:
			computedInfoList = [(t,'N/A') for t,f in requiredInfoList]
		infoTable = createHtmlInfoTable(computedInfoList )
		htmlMessage = gHtmlMessage.format(infoTable=infoTable)
		ui.browseableMessage(htmlMessage, title=pageTitle, isHtml= True)
	
	def getCurrCharFontName(self, info):
		formatConfig = {k:False for k,v in config.conf['documentFormatting'].iteritems()}
		formatConfig['reportFontName'] = True
		info=info.copy()
		info.expand(textInfos.UNIT_CHARACTER)
		for field in info.getTextWithFields(formatConfig):
			if isinstance(field,textInfos.FieldCommand) and isinstance(field.field,textInfos.FormatField):
				try:
					return field.field["font-name"]
				except KeyError:
					return None
		return None
