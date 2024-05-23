from pyfbsdk import*
from pyfbsdk_additions import*

try:
    from PySide6 import QtWidgets
except:
    from PySide2 import QtWidgets

from ui_mainwidget import Ui_toolWindow
import test
import makeList

class HoldedWidget(QtWidgets.QWidget, Ui_toolWindow):
    def __init__(self, pwidholder):
        super().__init__(pwidholder)
        self.setupUi(self)

        # add components of each comboBox
        self.comboBox.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5.addItem("") 
        
        self.shapeList = makeList.ReturnList
        for name in self.shapeList:
            self.comboBox.addItem(name)
            self.comboBox_2.addItem(name)
            self.comboBox_3.addItem(name)
            self.comboBox_4.addItem(name)
            self.comboBox_5.addItem(name)

        self.plycontrol = FBPlayerControl()

    def ChooseLyrics(self):
        self.lpopup = FBFilePopup()
        self.lpopup.Caption = "Select a file"
        self.lpopup.Style = FBFilePopupStyle.kFBFilePopupOpen
        self.lpopup.Filter = "*"
        self.lcheck = self.lpopup.Execute()
        self.lineEdit_2.setFontPointSize(11)
        if self.lcheck:
            if self.lpopup.FileName[-4:] == ".txt":
                f = open(self.lpopup.FileName, "r")
                data = f.readlines()
                for add_txt in data:
                    self.lineEdit_2.insertPlainText("\n" + add_txt)
            else:
                FBMessageBox("Caution","Error : Selected file is not text file.","OK")

    #def ConvertText(self):


    def Play(self):
        if self.plycontrol.IsPlaying:
            self.plycontrol.Stop()
        else:
            self.plycontrol.Play()