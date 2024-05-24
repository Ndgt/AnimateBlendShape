from pyfbsdk import*
from pyfbsdk_additions import*

try:
    from PySide6 import QtWidgets
except:
    from PySide2 import QtWidgets

from ui_mainwidget import Ui_toolWindow

import text
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

        # for player controls
        self.playcontrol = FBPlayerControl()
        self.startframe = self.playcontrol.LoopStart.GetFrame()
        self.endframe = self.playcontrol.LoopStop.GetFrame()


    '''
    Lyrics Edit methods
    '''
    def ChooseLyrics(self):
        self.lpopup = FBFilePopup()
        self.lpopup.Caption = "Select a file"
        self.lpopup.Style = FBFilePopupStyle.kFBFilePopupOpen
        self.lpopup.Filter = "*"
        self.lcheck = self.lpopup.Execute()
        if self.lcheck:
            # check if the file is text
            if self.lpopup.FileName[-4:] == ".txt":
                lyrics = text.ReadLyrics(self.lpopup.FileName)
                for line in lyrics.split("\n"):
                    self.lineEdit_2.append(line)
            else:
                FBMessageBox("Caution","Error : Selected file is not text file.","OK")

    def ConvertText(self):
        lyrics_converted = text.ConvertLyrics(self.lineEdit_2.toPlainText(),"hiragana")
        if not type(lyrics_converted) == ModuleNotFoundError:
            for line in lyrics_converted.split("\n"):
                self.lineEdit_2.append(line)


    '''
    player control methods 
    '''
    def Play(self):
        if self.playcontrol.IsPlaying:
            self.playcontrol.Stop()
        else:
            self.playcontrol.Play()

    def ChangePlaySpeed(self, spindouble):
        # if isPlaying, change speed and restart
        if self.playcontrol.IsPlaying:
            self.playcontrol.Stop()
            self.playcontrol.SetPlaySpeed(spindouble)
            self.playcontrol.Play()
        else:
            self.playcontrol.SetPlaySpeed(spindouble)

    def PlayerSlide(self, sliderint):
        # slider returns int : 0 ~ 99
        specified_frame_double = (self.endframe - self.startframe) * (sliderint / 100)
        specified_frame = int(specified_frame_double)
        # restart if isPlaying
        if self.playcontrol.IsPlaying:
            # set current frame (FBTime(0,0,0,specified frame))
            self.playcontrol.Goto(FBTime(0,0,0,specified_frame))
            self.playcontrol.Play()
        else:
            self.playcontrol.Goto(FBTime(0,0,0,specified_frame))