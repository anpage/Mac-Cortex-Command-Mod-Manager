#
#  main.py
#  MCCMM
#
#  Created by Frigid on 1/15/10.
#  Copyright __MyCompanyName__ 2010. All rights reserved.
#

#### DO NOT MODIFY ####
#import modules required by application
import objc
import Foundation
import AppKit
import BWToolkitFrameworkWrapper

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import MCCMMAppDelegate
import CCMMController

# pass control to AppKit
AppHelper.runEventLoop()
#### DO NOT MODIFY ####