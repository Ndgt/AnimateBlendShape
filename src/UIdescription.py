# -*- coding: utf-8

from pyfbsdk import*
from pyfbsdk_additions import*

try:
    from PySide6 import QtWidgets
    from PySide6.QtCore import Qt

except:
    from PySide2 import QtWidgets
    from PySide2.QtCore import Qt

from ui_mainwidget import Ui_toolWindow

import L_Edit

class HoldedWidget(QtWidgets.QWidget, Ui_toolWindow):
    def __init__(self, pwidholder):
        super().__init__(pwidholder)
        self.setupUi(self)

        # add characters in comboBox
        self.CharaComboBox.addItem("")
        for chara in FBSystem().Scene.Characters:
            self.CharaComboBox.addItem(chara.Name)
        self.CharaComboBox.currentIndexChanged.connect(self.updateComboBox)

        self.comboboxes = [self.comboBox,
                           self.comboBox_2,
                           self.comboBox_3,
                           self.comboBox_4,
                           self.comboBox_5]
        
        self.checkboxes = [self.checkBox,
                           self.checkBox_2,
                           self.checkBox_3,
                           self.checkBox_4,
                           self.checkBox_5]
        
        # connect signal with each checkbox
        for chbox in self.checkboxes:
            chbox.stateChanged.connect(lambda state, name: self.showFCurve(state, name))

        # for player controls
        self.playcontrol = FBPlayerControl()
        self.startframe = self.playcontrol.LoopStart.GetFrame()
        self.endframe = self.playcontrol.LoopStop.GetFrame()


    '''
    character shapekey methods
    '''
    # return All shapekey name in character user selected
    def ReturnCharaShape(self):
        mList = FBModelList()
        returnList = []
        # get current selected character
        chara = FBSystem().Scene.Characters.__getitem__(self.CharaComboBox.currentIndex()-1)
        
        # get all meshes related to the character
        chara.GetSkinModelList(mList)
        for mesh in mList:
            geo = mesh.Geometry
            for i in range(geo.ShapeGetCount()):
                name = geo.ShapeGetName(i)
                if not name in returnList:
                    returnList.append(name)
        return returnList


    # update character combobox when user select new item
    def updateComboBox(self):
        for cobox in self.comboboxes:
            cobox.clear()
            for shapekey in self.ReturnCharaShape():
                cobox.addItem(shapekey)


    # make the shapekey selected, and show in FCurve Editor
    # when the checkbox marked
    def showFCurve(self, state, name):
        chara = FBSystem().Scene.Characters.__getitem__(self.CharaComboBox.currentIndex()-1)
        mList = FBModelList()
        chara.GetSkinModelList(mList)
        plist = []
        for mesh in mList:
            prop = mesh.PropertyList.Find(name)
            plist.append(prop)

        if state == 2: 
            for shapekey in plist:
                shapekey.SetFocus(True)
        else:
            for shapekey in plist:
                shapekey.SetFocus(False)


    '''
    Lyrics Edit methods
    '''
    def ChooseLyrics(self):
        # display popup to select a file
        self.lpopup = FBFilePopup()
        self.lpopup.Caption = "Select a file"
        self.lpopup.Style = FBFilePopupStyle.kFBFilePopupOpen
        self.lpopup.Filter = "*"
        self.lcheck = self.lpopup.Execute()

        if self.lcheck:
            # check if the file is text file
            if self.lpopup.FileName[-4:] == ".txt":

                lyrics = L_Edit.ReadLyrics(self.lpopup.FileName)
                for line in lyrics.split("\n"):
                    self.LyricsText.append(line)
            else:
                FBMessageBox("Caution","Error : Selected file is not text file.","OK")


    def ConvertText(self):
        lyrics_converted = L_Edit.ConvertLyrics(self.LyricsText.toPlainText(),"hiragana")
        if not type(lyrics_converted) == ModuleNotFoundError:
            self.LyricsText.clear()
            for line in lyrics_converted.split("\n"):
                self.LyricsText.append(line)

    def SplitText(self):
        lyrics_converted = L_Edit.ConvertLyrics(self.LyricsText.toPlainText(),"alphabet")
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

