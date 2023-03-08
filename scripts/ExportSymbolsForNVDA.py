# -*- coding: UTF-8 -*-

#Snippet to modify char info __init__.py in order to export symbol dic.
#To be edited and integrated in __init__.py


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
		#Temp
		self.generateCharList()
	def generateCharList(self):
		def getNom(i):
			try:
				n = unicodeInfo.unicodeData['fr'][i][0].lower()
				n = n.replace('lettre majuscule cyrillique','')
				n = n.replace('lettre minuscule cyrillique', '')
				return n
			except KeyError:
				return 'NotAvailable'
		g = (unichr(i)+'\t'+getNom(i)+'\tnone\tnever' for i in range(1000, 2000))
		with open(r'h:\charlist.txt', 'w', encoding='utf8') as f:
			f.write('\r\n'.join(g))
