#!/usr/bin/env python

from ExtensionCore import ExtensionSidePage

class Module:
    def __init__(self, content_box):
        keywords = _("extension, addon")
        self.name = "extensions"
        self.comment = _("Manage your Cinnamon extensions")
        # for i18n replacement in ExtensionCore.py
        noun = _("extension")
        pl_noun = _("extensions")
        # we do not translate Cinnamon
        target = "Cinnamon"
        self.sidePage = ExtensionSidePage(_("Extensions"), "cs-extensions", keywords, content_box, "extension", noun, pl_noun, target, module=self)
        self.sidePage.RemoveString = ""
        self.category = "prefs"

    def on_module_selected(self):
        if not self.loaded:
            print "Loading Desklets module"
            self.sidePage.load()

    def _setParentRef(self, window, builder):
        self.sidePage.window = window
        self.sidePage.builder = builder

    def toSettingString(self, uuid, instanceId):
        return uuid

    def fromSettingString(self, string):
        return string

    def getAdditionalPage(self):
        return None

