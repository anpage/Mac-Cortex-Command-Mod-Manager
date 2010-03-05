#
#  CCMMController.py
#  MCCMM
#
#  Created by Frigid on 1/15/10.
#  Copyright (c) 2010 __MyCompanyName__. All rights reserved.
#
import os
from objc import IBAction
from Foundation import *
from Cocoa import * 

from ModScanner import ModScanner
import CCDir as ccDir

class CCMMController(NSObject):
    arrayMods = objc.IBOutlet('arrayMods')
    tableView = objc.IBOutlet('tableView')
    runBtn    = objc.IBOutlet('runBtn')
    
    CCDir = objc.ivar('CCDir')
    
    CCApp = objc.ivar('CCApp')
    CCPath = objc.ivar('CCPath')
    
    mods = objc.ivar('mods')
    
    def setRunBtnImage(self):
        self.runBtn.setLabel_(u"Run " + self.CCApp.split("/")[-1].split(".")[-2])
        print "Getting CC Icon..."
        print str(self.CCPath) + "ccosx.icns"
        if os.path.exists(str(self.CCPath) + "ccosx.icns"):
            print "Icon Found!"
            self.runBtn.setImage_(NSImage.alloc().initByReferencingFile_(str(self.CCPath) + "ccosx.icns"))
    
    def awakeFromNib(self):
        self.CCDir = ccDir.CCDir.alloc().init()
        
        self.CCApp = self.CCDir.getCCApp()
        
        self.CCPath = self.CCApp + "/Contents/Resources/"
        
        self.setRunBtnImage()
        
        self.mods = NSArray.alloc().init()
        
        self.scanMods_(None)
    
    @IBAction
    def runCC_(self, sender):
        os.system("open \""+self.CCApp+"\"")
        
    @IBAction
    def scanMods_(self, sender): 
        modScanner = ModScanner.alloc().init()
        
        modScanner.setModPath_(self.CCPath)
        
        self.mods = NSArray.alloc().initWithArray_(modScanner.getModArray())
        
        self.tableView.reloadData()
        
    @IBAction
    def getCCDir_(self, sender):
        self.CCApp = self.CCDir.getNewApp_(self.CCApp)
        self.CCPath = self.CCApp + "/Contents/Resources/"
        self.scanMods_(None)
        self.setRunBtnImage()
        
    @IBAction
    def checkBtn_(self, sender):
        print "Disabling " + str(self.mods[sender.selectedRow()]["modFolder"])
        
    def tableView_objectValueForTableColumn_row_(self, aTableView, aTableColumn, rowIndex):
        if rowIndex >= 0 and rowIndex < self.mods.count():
            
            theRecord = self.mods.objectAtIndex_(rowIndex)
            
            theValue = theRecord.objectForKey_(aTableColumn.identifier())
            
            return theValue
        else:
            NSAlert.alertWithMessageText_defaultButton_alternateButton_otherButton_informativeTextWithFormat_(
            u"Number of entries are mismatched. Contact app creator and report bug.", 
            None,
            None,
            None,
            u"rowIndex is less than or equal to 0, or smaller than the number of mods.")
    
    def numberOfRowsInTableView_(self, aTableView):
        if not self.mods:
            self.mods = NSArray.alloc().init()
            
        return self.mods.count()
