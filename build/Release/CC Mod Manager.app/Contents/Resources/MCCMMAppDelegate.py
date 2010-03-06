#
#  MCCMMAppDelegate.py
#  MCCMM
#
#  Created by Frigid on 1/15/10.
#  Copyright __MyCompanyName__ 2010. All rights reserved.
#

from Foundation import *
from AppKit import *

class MCCMMAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
