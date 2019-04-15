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
import inputCore
from logHandler import log
from characterProcessing import SpeechSymbols

import os
import re
from codecs import open

#import unicodedata

#Use unicodedata2 (Unicodedata backport for python 2/3 updated to the latest unicode version)
addonPath = os.path.dirname(__file__).decode("mbcs")
import sys
sys.path.append(os.path.join(addonPath, "unicodedata2"))
import unicodedata2 as unicodedata
del sys.path[-1]

import addonHandler

addonHandler.initTranslation()

pageTitle = _("Detailed character information'")
PLUGIN_DIR = os.path.dirname(__file__).decode('mbcs')
DATA_DIR = os.path.join(PLUGIN_DIR, "locale")
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
	titleLabel = _("Attribute")
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
	(_("Character"), 'getCharStr'),
	(_("Name"), 'getNameStr'),
	(_("CLDR name"), 'getCldrNameStr'),
	(_("Decimal value"), 'getDecStr'),
	(_("Hex value"), 'getHexStr'),
	(_("Category"), 'getCategoryStr'),
	(_("Block"), 'getBlockStr'),
	]

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

class Character(object):

	def __init__(self, cNum, cText):
		super(Character, self).__init__()
		self.num = cNum
		self.text = cText
		if self.num >= 0x10000:
		#For NVDA < 2019.1 that does not support 32-bit char
			s = "\\U%08x" % self.num
			self.text = s.decode('unicode-escape')
		
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
		commands.script_review_currentCharacter.im_func.__doc__ = ""
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
		commands.script_review_currentCharacter.im_func.__doc__ = self.biScriptDoc
		#Clear charInfo plugin gestures
		self.clearGestureBindings()
		
	def script_review_currentCharacter(self,gesture):
		scriptCount=scriptHandler.getLastScriptRepeatCount()
		if scriptCount >= 4:
			return
		elif scriptCount <= 2:
			commands.script_review_currentCharacter(gesture)
			return
		
		### Code copied from NVDA script_review_currentCharacter in file globalCommands.py
		info=api.getReviewPosition().copy()
		info.expand(textInfos.UNIT_CHARACTER)
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
			char = Character(c, info.text)
			computedInfoList = [(t, getattr(char, f)()) for t,f in requiredInfoList]
		else:
			computedInfoList = [(t,'N/A') for t,f in requiredInfoList]
		infoTable = createHtmlInfoTable(computedInfoList )
		htmlMessage = gHtmlMessage.format(infoTable=infoTable)
		ui.browseableMessage(htmlMessage, title=pageTitle, isHtml= True)
	script_review_currentCharacter.__doc__ = commands.script_review_currentCharacter.__doc__ + _(". Pressing four times presents a message with detailed information on this character.")
	script_review_currentCharacter.category = commands.script_review_currentCharacter.category
	


