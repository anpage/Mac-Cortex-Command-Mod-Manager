#
#  ModScanner.py
#  MCCMM
#
#  Created by Frigid on 1/23/10.
#  Copyright (c) 2010 __MyCompanyName__. All rights reserved.
#

from Foundation import *
import os
import fileinput

BUILTIN = ["Base.rte", "Browncoats.rte", "Coalition.rte", "Dummy.rte", "Missions.rte", "Ronin.rte",
"Tutorial.rte", "Undead.rte", "Whitebots.rte", "Wildlife.rte"]

class ModScanner(NSObject):
    ModPath = objc.ivar(u"ModPath")
    
    def getModArray(self):
        enabled = self.getMods(self.ModPath, True)
        disabled = self.getMods(str(self.ModPath) + "Disabled_Mods/", False)
        
        modarray = enabled + disabled
        
        return modarray
    
    def setModPath_(self, path):
        self.ModPath = path
        
    def getMods(self, path, enabled):
        print "Scanning for mods in " + path + ":"
        
        if not os.path.isdir(path):
            print "Directory doesn't exist: " + path + ", creating..."
            os.mkdir(path)
        
        Mods = os.listdir(path)
        
        ModNames = []
        
        ModArray = []
        
        for i, directory in enumerate(Mods[:]):
            BuiltIn = False
            
            for BIMod in BUILTIN:
                if BIMod == directory:
                    BuiltIn = True
            
            if not directory.endswith(".rte"):
                print directory + " - Not a mod."
                Mods.remove(directory)
            elif BuiltIn:
                print directory + " - Is Built-In. Will Ignore."
                Mods.remove(directory)
            else:
                nameFound = False
                for line in fileinput.input(path+directory+"/index.ini"):
                    if not line.find("ModuleName") == -1:
                        table = line.split("=")
                        ModNames.append(table[1].strip())
                        print "Mod Found - " + table[1].strip()
                        fileinput.close()
                        nameFound = True
                        break
                if nameFound == False:
                    ModNames.append(directory.split(".rte")[0])
        
        for i, v in enumerate(Mods):
            if os.path.exists(path + v + "/ModuleIcon.bmp"):
                image = NSImage.alloc().initByReferencingFile_(path + v + "/ModuleIcon.bmp")
            else:
                image = NSImage.alloc().initByReferencingFile_(NSBundle.mainBundle().pathForResource_ofType_(u"noicon", u"png"))
            
            dict = NSMutableDictionary.dictionaryWithDictionary_({u"modIsEnabled":     enabled,
                                                                  u"modIcon":          image,
                                                                  u"modName":          ModNames[i],
                                                                  u"modFolder":        v})
                                                           
            ModArray.append(dict)
            
        return ModArray