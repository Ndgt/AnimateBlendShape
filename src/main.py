from pyfbsdk import*
from pyfbsdk_additions import*
try:
    from PySide6 import QtWidgets
    from shiboken6 import wrapInstance, getCppPointer
except:
    from PySide2 import QtWidgets
    from shiboken2 import wrapInstance, getCppPointer

# get file path for module import 
import sys, os, inspect
CurrentFilePath = inspect.currentframe().f_code.co_filename
sys.path.append(os.path.dirname(CurrentFilePath))

# import file describes UI
import UIdescription

# declare WidgetHolder class object
class WigHolder(FBWidgetHolder):
    # override C++ API WidgetCreate function
    def WidgetCreate(self, pWigParent):
        self.HoldedWidgetObject = UIdescription.HoldedWidget(wrapInstance(pWigParent,
                                                             QtWidgets.QWidget))
        return getCppPointer(self.HoldedWidgetObject)[0]

# declare as FBTool 
class WigTool(FBTool):
    def PopulateLayout(self):
        # Secure Layout for Input Control / Qt 
        x = FBAddRegionParam(0, FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(0, FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(0, FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(0, FBAttachType.kFBAttachHeight,"")
        self.AddRegion("InputControl", "InputControl", x,y,w,h)
        self.SetControl("InputControl", self.WigHolderObject)

    def __init__(self,name):
        super().__init__(name)
        self.WigHolderObject = WigHolder()
        self.PopulateLayout()
        self.StartSizeX = 900
        self.StartSizeY = 710
        self.Editor = FBFCurveEditor()
        self.face = FBFindModelByLabelName("Face")
        self.aprop = self.face.PropertyList.Find("a",False)
        self.pNode = self.aprop.GetAnimationNode()
        self.Editor.AddProperty(self.aprop)
 
        # Secure Layout for FBFCurvesEditor
        x = FBAddRegionParam(0, FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(360, FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(0, FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(0, FBAttachType.kFBAttachBottom,"")
        self.AddRegion("FCurveEditor", "FCurveEditor",x,y,w,h)
        self.SetControl("FCurveEditor", self.Editor)

# define tool name
toolName = "AnimateBlendShape"

# Delete Tool if exists
FBDestroyToolByName(toolName)

tool = WigTool(toolName)
FBAddTool(tool)
ShowTool(tool)