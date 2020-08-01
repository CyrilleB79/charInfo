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
from globalCommands import SCRCAT_TEXTREVIEW, commands
import api
import speech
import textInfos

import unicodedata
import os
import re
from codecs import open

import addonHandler

addonHandler.initTranslation()

pageTitle = _("Detailed character information'")
PLUGIN_DIR = os.path.dirname(__file__).decode('mbcs')
DATA_DIR = os.path.join(PLUGIN_DIR, "data")
BLOCK_FILE = "Blocks.txt"
PROP_VAL_ALIAS_FILE = "PropertyValueAliases.txt"

def mkhi(itemType, content, attribDic={}):
	"""Creates an HTML element."""
	sAttribs = ''.join(' ' + n + '=' + v for n,v in attribDic.items())
	return '<' + itemType + sAttribs + '>' + content + '</' + itemType + '>'
	
def createHtmlInfoTable(infoList):
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

gHtmlMessage = '<!doctype html>' + \
	mkhi('html',
	mkhi('head', '<meta charset= "utf-8"/>' + mkhi('style', css)) + 
	mkhi('body',
	mkhi('h1', pageTitle)
	+ '{infoTable}'))
	


def getCharValue(c,t):
	return t
def getNameValue(c,t):
	try:
		return unicodedata.name(unichr(c))
	except ValueError:
		return None
def getDecValue(c,t):
	return str(c)
def getHexValue(c,t):
	return hex(c)
def getCategoryValue(c,t):
	cat = unicodedata.category(unichr(c))
	return cat + ' - ' + unicodeInfo.generalCategories[cat]

def getBlockValue(c, t):
	for inf,sup,name in unicodeInfo.blocks:
			if inf <= c <= sup:
				return name
	return None
	

def makeSafe(f):
	def safeFun(*a, **kw):
		try:
			return f(*a, **kw)
		except:
			return 'N/A'
	return safeFun
		

infoList = [
	(_("Character"), makeSafe(getCharValue)),
	(_("Name"), lambda c,t: unicode(getNameValue(c,t))),
	(_("Decimal value"), getDecValue),
	(_("Hex value"), getHexValue),
	(_("Category"), makeSafe(getCategoryValue)),
	(_("Block"), getBlockValue),
	]

class UnicodeInfo(object):

	blocks = None
	
	def __init__(self):
		super(UnicodeInfo, self).__init__()
		self.blocks = self._getBlockInfo()
		self.generalCategories = self._getGeneralCategoryInfo()
	
	@staticmethod
	def _getBlockInfo():
		filePath = os.path.join(DATA_DIR, BLOCK_FILE)
		rc = re.compile(r'^([0-9A-F]+)\.\.([0-9A-F]+); ([- \w]+)$')
		lBlocks = []
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
		
	@staticmethod
	def _getGeneralCategoryInfo():
		filePath = os.path.join(DATA_DIR, PROP_VAL_ALIAS_FILE)
		#rc = re.compile(r'^(\w+) *; *(\w+) *; *([-\w]+) *(?:#.*)$')
		rc = re.compile(r'^(gc) *; *(\w+) *; *([- \w]+) *(?:#.*)?$')
		
		dicData = {}
		with open(filePath, 'r', encoding='UTF-8') as f:
			for l in (ll.strip() for ll in f):
				if (l.startswith('#')
				or len(l) == 0):
					continue
				m = rc.match(l)
				#if not m: raise ValueError(l)
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

unicodeInfo = UnicodeInfo()
		
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		
	def script_review_currentCharacter(self,gesture):
		scriptCount=scriptHandler.getLastScriptRepeatCount()
		if scriptCount >= 4:
			return
		elif scriptCount <= 2:
			commands.script_review_currentCharacter(gesture)
			return
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
		if c is not None:
			computedInfoList = [(t,f(c, info.text)) for t,f in infoList]
		else:
			computedInfoList = [(t,'N/A') for t,f in infoList]
		infoTable = createHtmlInfoTable(computedInfoList )
		htmlMessage = gHtmlMessage.format(infoTable=infoTable)
		ui.browseableMessage(htmlMessage, title=pageTitle, isHtml= True)
	script_review_currentCharacter.__doc__ = commands.script_review_currentCharacter.__doc__ + _(". Pressing four times presents a message with detailed characteristics of this character.")
	script_review_currentCharacter.category = commands.script_review_currentCharacter.category
	
	__gestures = {k:v for k,v in commands._GlobalCommands__gestures.items() if v == 'review_currentCharacter'}
	#import inputCore
	#self.gestures = inputCore.manager.getAllGestureMappings(obj=gui.mainFrame.prevFocus, ancestors=gui.mainFrame.prevFocusAncestors)
	#ou
	#a=inputCore.manager.getAllGestureMappings()
	#ll=a.values()
	#o=[e for e in ll[1].values() if e.scriptName=='review_currentCharacter' ]
	
	
