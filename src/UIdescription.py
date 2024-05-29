from pyfbsdk import*
from pyfbsdk_additions import*

try:
    from PySide6 import QtWidgets
except:
    from PySide2 import QtWidgets

from ui_mainwidget import Ui_toolWindow

import text

class HoldedWidget(QtWidgets.QWidget, Ui_toolWindow):
    def SpaceKeyInput(self, control, eventKey):
        self.LyricsText.append(eventKey.Key+" "+eventKey.X+" ",eventKey.Y)

    def __init__(self, pwidholder):
        super().__init__(pwidholder)
        self.setupUi(self)

        self.sys = FBSystem()
        self.UIhandle  = self.sys.OnUIIdle

        # add characters in comboBox
        self.CharaComboBox.addItem("")
        for chara in FBSystem().Scene.Characters:
            self.CharaComboBox.addItem(chara)
            self.CharaComboBox.setItemText(self.CharaComboBox.count,chara.Name)
        self.CharaComboBox.currentIndexChanged().connect(self.updateComboBox)

        # for player controls
        self.playcontrol = FBPlayerControl()
        self.startframe = self.playcontrol.LoopStart.GetFrame()
        self.endframe = self.playcontrol.LoopStop.GetFrame()

        # for key inputs
        self.playButton.OnInput.Add(self.SpaceKeyInput)
 
    def ReturnCharaShape(self, chara:FBCharacter, mList):
        returnList = list()
        chara.GetSkinModelList(mList)
        for mesh in mList:
            geo = mesh.Geometry
            for i in range(geo.ShapeGetCount()):
                name = geo.ShapeGetName(i)
                if not name in returnList:
                    returnList.append(name)
        return returnList


    def updateComboBox(self, index):
        for cbox in [self.comboBox,
                     self.comboBox_2,
                     self.comboBox_3,
                     self.comboBox_4,
                     self.comboBox_5]:
            cbox.clear()
            for skey in self.ReturnCharaShape(self.CharaComboBox.currentData):
                cbox.addItem(skey)


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
                    self.LyricsText.append(line)
            else:
                FBMessageBox("Caution","Error : Selected file is not text file.","OK")


    def ConvertText(self):
        lyrics_converted = text.ConvertLyrics(self.LyricsText.toPlainText(),"hiragana")
        if not type(lyrics_converted) == ModuleNotFoundError:
            self.LyricsText.clear()
            for line in lyrics_converted.split("\n"):
                self.LyricsText.append(line)

    def SplitText(self):
        lyrics_converted = text.ConvertLyrics(self.LyricsText.toPlainText(),"alphabet")
        if not type(lyrics_converted) == ModuleNotFoundError:
            self.LyricsText.clear()
            # set vowel list
            vowels = ["a","i","u","e","o"]
            for line in lyrics_converted.split("\n"):
                finalline = " "
                # omit consonant from line
                for char in line:
                    finalline += char
                    if char in vowels:
                        finalline += "/"                
                self.LyricsText.append(finalline)

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