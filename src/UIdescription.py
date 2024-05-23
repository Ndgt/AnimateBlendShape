from pyfbsdk import*
from pyfbsdk_additions import*

try:
    from PySide6 import QtWidgets
except:
    from PySide2 import QtWidgets

from ui_mainwidget import Ui_toolWindow
import test

class HoldedWidget(QtWidgets.QWidget, Ui_toolWindow):
    def __init__(self, pwidholder):
        super().__init__(pwidholder)
        self.setupUi(self)
        self.plycontrol = FBPlayerControl()


    def ChooseLyrics(self):
        self.lpopup = FBFilePopup()
        self.lpopup.Caption = "Select a file"
        self.lpopup.Style = FBFilePopupStyle.kFBFilePopupOpen
        self.lpopup.Filter = "*"
        self.lcheck = self.lpopup.Execute()
        if self.lcheck:
            if self.lpopup.FIleName[-4:] == ".txt":
                f = open(self.lpopup.FileName, "r")
                data = f.readlines()
                for add_txt in data:
                    current_txt = self.lineEdit_2.text()
                    self.lineEdit_2.setText(current_txt+add_txt)
            else:
                FBMessageBox("Caution","Error : Selected file is not text file.","OK")

    #def ConvertText(self):


    def Play(self):
        if self.plycontrol.IsPlaying:
            self.plycontrol.Stop()
        else:
            self.plycontrol.Play()