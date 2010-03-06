#
#  CCDir.py
#  CC Mod Manager
#
#  Created by Frigid on 1/25/10.
#  Copyright (c) 2010 __MyCompanyName__. All rights reserved.
#
import os

from Foundation import *
from Cocoa import NSOKButton

class CCDir(NSObject):
    
    def getCCApp(self):
        CCDir = None
        
        settingsFilePath = str(NSBundle.mainBundle().resourcePath()) + "/settings.cfg"
        
        print "SETTINGS FILE: " + settingsFilePath
        if os.path.exists(settingsFilePath):
            settingsFile = open(settingsFilePath,"r")
            CCDir = settingsFile.readlines()[0].split("=")[1].strip()
            settingsFile.close()
            
            if not os.path.exists(CCDir):
                CCDir = None
            
        if os.path.isdir("/Applications/Cortex Command.app") and CCDir == None:
            CCDir = "/Applications/Cortex Command.app"
        
        if CCDir == None:
            openDlg = NSOpenPanel.openPanel()

            openDlg.setCanChooseFiles_(True)
            
            openDlg.setAllowsMultipleSelection_(False)
            
            openDlg.setTitle_("Please select the Cortex Command app to modify:")

            if openDlg.runModalForDirectory_file_types_(u"/Applications", None, (u"app",)) == NSOKButton:
                CCDir = str(openDlg.filename())
            else:
                CCDir = None
        
        if not CCDir == None:
            print "Settings file: " + settingsFilePath
            settingsFile = open(settingsFilePath,"w")
            settingsFile.write("CCDIR = " + CCDir)
            settingsFile.close()
                
        return CCDir
        
    def getNewApp_(self, oldPath):
        
        settingsFilePath = str(NSBundle.mainBundle().resourcePath()) + "/settings.cfg"
        
        openDlg = NSOpenPanel.openPanel()

        openDlg.setCanChooseFiles_(True)
            
        openDlg.setAllowsMultipleSelection_(False)
        
        openDlg.setTitle_("Please select the Cortex Command app to modify:")

        if openDlg.runModalForDirectory_file_types_(u"/Applications", None, (u"app",)) == NSOKButton:
            CCDir = str(openDlg.filename())
        else:
            CCDir = oldPath
                
        print self.settingsFilePath
        settingsFile = open(settingsFilePath,"w")
        settingsFile.write("CCDIR = " + CCDir)
        settingsFile.close()
        
        return CCDir
            