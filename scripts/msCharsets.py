# -*- coding: UTF-8 -*-
#A tool script for NVDA add-on Character information
#This script get the tables containing specific Microsoft character sets and their unicode equivalents.
#from http://www.alanwood.net/
#The Microsoft charsets that are retrieved from this website are: wingdings, wingdings 2, wingdings 3, webdings and symbol.
#Copyright (C) 2019 Cyrille Bougot
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.

from __future__ import absolute_import, division, print_function, unicode_literals

from urllib.request import urlopen
import re
from lxml import etree

urlBase = "http://www.alanwood.net/demos/"
charsetList = [
	'wingdings',
	'wingdings-2',
	'wingdings-3',
	'webdings',
	'symbol',
	]

def getPageTree(url):
	response = urlopen(url)
	s = response.read()
	return etree.HTML(s)

def getTable(html, nTable):
	tableNodes = html.xpath('//table')
	trNodes = tableNodes[nTable].xpath('.//tr')
	content = [[e.text for e in tr.xpath('*[self::td or self::th]')] for tr in trNodes]
	return content

def getTable2(html, nTable):
	tableNodes = html.xpath('//table')
	trNodes = tableNodes[nTable].xpath('.//tr')
	getTdText = lambda td: td.text if td.text is not None else td.xpath('*/text()')
	content = []
	for tr in trNodes:
		contentTR = [getTdText(td) for td in tr.xpath('td')]
		content.append(contentTR)
	return content

def getTableDings(url):
	html = getPageTree(url)
	t = getTable(html, 0)
	allCharInfo = []
	for l in t[2:]:
		numMS = l[1]
		nameMS = l[3]
		try:
			numUnicode = int(l[5])
		except (IndexError, TypeError):
			numUnicode = None
		charInfo = [str(numMS), nameMS, str(numUnicode)]
		allCharInfo.append(charInfo)
	return allCharInfo
	
def getAllTableSymbol(url):
	fullTable = []
	for nTable in range(1,40):
		try:
			fullTable.extend(getTableSymbol(url, nTable))
		except IndexError:
			break
	fullTable.sort(key=lambda x:int(x[0]))	
	return fullTable
	
def getTableSymbol(url, nTable):
	html = getPageTree(url)
	t = getTable2(html, nTable)
	htmlNumPattern = r'&#(?P<num>\d+);'
	allCharInfo = []
	for l in t[2:]:
		if l[2] == 'space':
			numMS = 32 #space
			nameMS = l[2]
			fieldNumUnicode = l[4]
		else:
			numMS = ord(l[0][0])
			nameMS = l[2]
			fieldNumUnicode = l[4]
		m = re.match(htmlNumPattern, fieldNumUnicode)
		numUnicode = int(m.groupdict()['num'])
		charInfo = [str(numMS), nameMS, str(numUnicode)]
		allCharInfo.append(charInfo)
	return allCharInfo
	
def generateTableChar(charset):
	url = urlBase + charset + '.html'
	if charset == 'symbol':
		allCharInfo = getAllTableSymbol(url)
	else:
		allCharInfo = getTableDings(url)
	with open(charset + '.txt', 'wt', encoding='utf-8') as f:
		for charInfo in allCharInfo:
			s = '\t'.join(charInfo) + '\n'
			f.write(s)

for cs in charsetList:
	generateTableChar(cs)
