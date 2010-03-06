import shutil
import os

def ensureDisabledDir(CCDir):
    dirname = "Disabled_Mods"
    if not os.path.isdir(CCDir + dirname + "/"):
        print "Directory doesn't exist: " + CCDir + dirname + "/"
        os.mkdir(CCDir + dirname + "/")

def disableMod(CCDir, modname):
    ensureDisabledDir(CCDir)
    shutil.move(CCDir + modname, CCDir + "Disabled_Mods/" + modname)
    
def enableMod(CCDir, modname):
    ensureDisabledDir(CCDir)
    shutil.move(CCDir + "Disabled_Mods/" + modname, CCDir + modname)
