import objc
from Foundation import NSBundle

objc.loadBundle("BWToolkitFramework",
                globals(),
                bundle_path=objc.pathForFramework(
                NSBundle.mainBundle().privateFrameworksPath() + u'/BWToolkitFramework.framework'))