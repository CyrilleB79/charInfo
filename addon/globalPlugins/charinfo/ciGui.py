# -*- coding: UTF-8 -*-
# NVDA add-on: Character Information
# Copyright (C) 2023 Cyrille Bougot
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

from gui import guiHelper, nvdaControls, settingsDialogs
import config
from logHandler import log
import globalPluginHandler
import wx

import addonHandler

addonHandler.initTranslation()

ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]


class CharInfoSettingsPanel(settingsDialogs.SettingsPanel):
	title = ADDON_SUMMARY

	actionNPressesLabels = (
		# Translators: An option in an action definition combobox Character Information setting panel.
		('speakCharacter', _('Report the character')),
		# Translators: An option in an action definition combobox Character Information setting panel.
		('speakCharacterDescription', _('Report the character description')),
		# Translators: An option in an action definition combobox Character Information setting panel.
		('speakCharacterNum', _('Report the character number')),
		# Translators: An option in an action definition combobox Character Information setting panel.
		('displayCurrentCharInfoMessage', _('Display information on the character')),
		# Translators: An option in an action definition combobox Character Information setting panel.
		('speakCLDRLocaleName', _('Report the CLDR locale name of the character')),
		# Translators: An option in an action definition combobox Character Information setting panel.
		('speakCLDREnglishName', _('Report the CLDR English name of the character')),
		# Translators: An option in an action definition combobox Character Information setting panel.
		('speakCharacterLocaleName', _('Report the locale name of the character')),
		# Translators: An option in an action definition combobox Character Information setting panel.
		('speakCharacterEnglishName', _('Report the English name of the character')),
		# Translators: An option in an action definition combobox Character Information setting panel.
		('speakMSChar', _('Report Microsoft font proprietary character (name, font and equivalent Unicode name)')),
		
	)

	def makeSettings(self, settingsSizer):
		# Check that options in the GUI are the same as the ones in the config
		configChoices = config.conf.getConfigValidation(('charInfo', 'action2Presses')).args
		if not set(configChoices) == set(o for (o, s) in self.actionNPressesLabels):
			log.error('Options mismatch in charInfo settings panel')

		sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		
		# Translators: This is the label for a group of action choices in the add-on's settings panel
		actionGroupText = _("Action for multiple presses of the report review character command")
		actionGroupSizer = wx.StaticBoxSizer(wx.VERTICAL, self, label=actionGroupText)
		actionGroupBox = actionGroupSizer.GetStaticBox()
		self.actionGroup = guiHelper.BoxSizerHelper(self, sizer=actionGroupSizer)
		sHelper.addItem(self.actionGroup)

		self.actionNPressesComboboxes = []
		for nPresses in (2, 3, 4):
			self.actionNPressesComboboxes.append(self.makeActionNPressCombobox(nPresses))

		self.lockActionDuringCharNavCheckBox = sHelper.addItem(
			# Translators: This is the label for a checkbox in the Character Information settings panel.
			wx.CheckBox(self, label=_("Remember these action during character navigation"))
		)
		self.lockActionDuringCharNavCheckBox.SetValue(config.conf['charInfo']['lockActionDuringCharNav'])

	def makeActionNPressCombobox(self, nPresses):
		# Translators: This is the label for the action definition comboboxes in the Character Information settings panel.
		actionNPressesText = _("{n} presses:").format(n=nPresses)
		actionNPressesChoices = [name for setting, name in self.actionNPressesLabels]
		actionNPressesCombobox = self.actionGroup.addLabeledControl(
			actionNPressesText,
			wx.Choice,
			choices=actionNPressesChoices,
		)
		for index, (setting, name) in enumerate(self.actionNPressesLabels):
			if setting == config.conf['charInfo'][f'action{nPresses}Presses']:
				actionNPressesCombobox.SetSelection(index)
				break
		else:
			log.debugWarning(f"Could not set actionNPressesCombobox ({nPresses}) to current setting")
		actionNPressesCombobox.Bind(wx.EVT_CHOICE, self.onActionNPressesChange)
		return actionNPressesCombobox

	def onActionNPressesChange(self, evt):
		enable = True
		for nPresses in (2, 3, 4):
			self.actionNPressesComboboxes[nPresses - 2].Enable(enable)
			if self.actionNPressesLabels[
				self.actionNPressesComboboxes[nPresses - 2].GetSelection()
			][0] == 'displayCurrentCharInfoMessage':
				# Disable subsequent comboboxes
				enable = False

	def onSave(self):
		for nPresses in (2, 3, 4):
			config.conf['charInfo'][f'action{nPresses}Presses'] = self.actionNPressesLabels[
				self.actionNPressesComboboxes[nPresses - 2].GetSelection()
			][0]
		config.conf['charInfo']['lockActionDuringCharNav'] = self.lockActionDuringCharNavCheckBox.IsChecked()
