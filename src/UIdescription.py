from pyfbsdk import*
from pyfbsdk_additions import*

try:
    from PySide6 import QtWidgets
except:
    from PySide2 import QtWidgets

from ui_mainwidget import Ui_toolWindow

class HoldedWidget(QtWidgets.QWidgetm, Ui_toolWindow):
    def __init__(self, pwidholder):
        super().__init__(pwidholder)
        self.setupUi(self)

        self.Editor = FBFCurveEditor()
        self.face = FBFindModelByLabelName("Face")
        self.aprop = self.face.PropertyList.Find("a",False)
        self.pNode = self.aprop.GetAnimationNode()
        self.Editor.AddProperty(self.aprop)

        self.SetControl(self.FCurveEditorLayout,self.Editor)