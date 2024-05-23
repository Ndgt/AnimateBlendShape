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
        
        self.shapeList = makeList.ReturnList()
        for name in self.shapeList:
            self.comboBox.addItem(name)
            self.comboBox_2.addItem(name)
            self.comboBox_3.addItem(name)
            self.comboBox_4.addItem(name)
            self.comboBox_5.addItem(name)

        # player controls
        self.playcontrol = FBPlayerControl()
        self.startframe = self.playcontrol.LoopStart.GetFrame()
        self.endframe = self.playcontrol.LoopStop.GetFrame()

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
        if self.playcontrol.IsPlaying:
            self.playcontrol.Stop()
        else:
            self.playcontrol.Play()

    def ChangePlaySpeed(self, double):
        # if isPlaying, change speed and restart
        if self.playcontrol.IsPlaying:
            self.playcontrol.Stop()
            self.playcontrol.SetPlaySpeed(double)
            self.playcontrol.Play()
        else:
            self.playcontrol.SetPlaySpeed(double)

    def PlayerSlide(self,int):
        # slider returns int : 0 ~ 99
        current_frame_double = (self.endframe - self.startframe) * (int / 100)
        # restart if isPlaying
        if self.playcontrol.IsPlaying:
            # set current frame (FBTime(0,0,0,specified frame))
            self.playcontrol.Goto(FBTime(0,0,0,int(current_frame_double)))
            self.playcontrol.Play
        else:
            self.playcontrol.Goto(FBTime(0,0,0,int(current_frame_double)))