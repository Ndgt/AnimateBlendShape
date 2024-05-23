from pyfbsdk import*
from pyfbsdk_additions import*

try:
    from PySide6 import QtWidgets
except:
    from PySide2 import QtWidgets

from ui_mainwindow import Ui_MainWindow

class HoldedWidget(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self, pwidholder):
        super().__init__(pwidholder)
        self.setupUi(self)
        self.plycontrol = FBPlayerControl()

    def Play(self):
        if self.plycontrol.IsPlaying:
            self.plycontrol.Stop()
        else:
            self.plycontrol.Play()