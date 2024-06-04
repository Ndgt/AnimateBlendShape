# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6 import QtCore
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit, QTextEdit
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QTabWidget, QVBoxLayout, QWidget)

class Ui_toolWindow(object):
    def setupUi(self, toolWindow):
        if not toolWindow.objectName():
            toolWindow.setObjectName(u"toolWindow")
        toolWindow.resize(900, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(toolWindow.sizePolicy().hasHeightForWidth())
        toolWindow.setSizePolicy(sizePolicy)
        toolWindow.setMaximumSize(QSize(16777215, 600))
        self.horizontalLayout_4 = QHBoxLayout(toolWindow)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, -1, -1, -1)
        self.tabWidget = QTabWidget(toolWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_12 = QVBoxLayout(self.tab_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ChooseLyricsButton = QPushButton(self.tab_2)
        self.ChooseLyricsButton.setObjectName(u"ChooseLyricsButton")

        self.horizontalLayout_2.addWidget(self.ChooseLyricsButton)

        self.ToHiraganaButton = QPushButton(self.tab_2)
        self.ToHiraganaButton.setObjectName(u"ToHiraganaButton")

        self.horizontalLayout_2.addWidget(self.ToHiraganaButton)

        self.ToAlphabetButton = QPushButton(self.tab_2)
        self.ToAlphabetButton.setObjectName(u"ToAlphabetButton")

        self.horizontalLayout_2.addWidget(self.ToAlphabetButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_2)

        self.LyricsText = QTextEdit(self.tab_2)
        self.LyricsText.setObjectName(u"LyricsText")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.LyricsText.sizePolicy().hasHeightForWidth())
        self.LyricsText.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(11)
        self.LyricsText.setFont(font)

        self.verticalLayout_11.addWidget(self.LyricsText)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_3.addWidget(self.tabWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 5, -1)
        self.SelectShapeKeyGroupBox = QGroupBox(toolWindow)
        self.SelectShapeKeyGroupBox.setObjectName(u"SelectShapeKeyGroupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.SelectShapeKeyGroupBox.sizePolicy().hasHeightForWidth())
        self.SelectShapeKeyGroupBox.setSizePolicy(sizePolicy3)
        self.SelectShapeKeyGroupBox.setFlat(False)
        self.verticalLayout_10 = QVBoxLayout(self.SelectShapeKeyGroupBox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.SelectShapeKeyGroupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(self.SelectShapeKeyGroupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.SelectShapeKeyGroupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.SelectShapeKeyGroupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.SelectShapeKeyGroupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(self.SelectShapeKeyGroupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.label_8)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.CharaComboBox = QComboBox(self.SelectShapeKeyGroupBox)
        self.CharaComboBox.setObjectName(u"CharaComboBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.CharaComboBox.sizePolicy().hasHeightForWidth())
        self.CharaComboBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.CharaComboBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBox_1 = QComboBox(self.SelectShapeKeyGroupBox)
        self.comboBox_1.setObjectName(u"comboBox_1")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.comboBox_1.sizePolicy().hasHeightForWidth())
        self.comboBox_1.setSizePolicy(sizePolicy6)

        self.verticalLayout_4.addWidget(self.comboBox_1)

        self.comboBox_2 = QComboBox(self.SelectShapeKeyGroupBox)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy6.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy6)

        self.verticalLayout_4.addWidget(self.comboBox_2)

        self.comboBox_3 = QComboBox(self.SelectShapeKeyGroupBox)
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy6.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy6)

        self.verticalLayout_4.addWidget(self.comboBox_3)

        self.comboBox_4 = QComboBox(self.SelectShapeKeyGroupBox)
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy6.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy6)

        self.verticalLayout_4.addWidget(self.comboBox_4)

        self.comboBox_5 = QComboBox(self.SelectShapeKeyGroupBox)
        self.comboBox_5.setObjectName(u"comboBox_5")
        sizePolicy6.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy6)

        self.verticalLayout_4.addWidget(self.comboBox_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.checkBox_1 = QCheckBox(self.SelectShapeKeyGroupBox)
        self.checkBox_1.setObjectName(u"checkBox_1")
        sizePolicy.setHeightForWidth(self.checkBox_1.sizePolicy().hasHeightForWidth())
        self.checkBox_1.setSizePolicy(sizePolicy)
        self.checkBox_1.setTristate(False)

        self.verticalLayout_8.addWidget(self.checkBox_1)

        self.checkBox_2 = QCheckBox(self.SelectShapeKeyGroupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)

        self.verticalLayout_8.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.SelectShapeKeyGroupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)

        self.verticalLayout_8.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.SelectShapeKeyGroupBox)
        self.checkBox_4.setObjectName(u"checkBox_4")
        sizePolicy.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy)

        self.verticalLayout_8.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.SelectShapeKeyGroupBox)
        self.checkBox_5.setObjectName(u"checkBox_5")
        sizePolicy.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy)

        self.verticalLayout_8.addWidget(self.checkBox_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)


        self.horizontalLayout.addLayout(self.verticalLayout_9)


        self.verticalLayout_10.addLayout(self.horizontalLayout)


        self.verticalLayout_6.addWidget(self.SelectShapeKeyGroupBox)

        self.PlayerControlGroupBox = QGroupBox(toolWindow)
        self.PlayerControlGroupBox.setObjectName(u"PlayerControlGroupBox")
        sizePolicy3.setHeightForWidth(self.PlayerControlGroupBox.sizePolicy().hasHeightForWidth())
        self.PlayerControlGroupBox.setSizePolicy(sizePolicy3)
        self.PlayerControlGroupBox.setFlat(False)
        self.PlayerControlGroupBox.setCheckable(False)
        self.verticalLayout_5 = QVBoxLayout(self.PlayerControlGroupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 1, -1, 1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.playButton = QPushButton(self.PlayerControlGroupBox)
        self.playButton.setObjectName(u"playButton")
        sizePolicy3.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())
        self.playButton.setSizePolicy(sizePolicy3)

        self.horizontalLayout_9.addWidget(self.playButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.PlayerControlGroupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.playspeedSpinBox = QDoubleSpinBox(self.PlayerControlGroupBox)
        self.playspeedSpinBox.setObjectName(u"playspeedSpinBox")
        sizePolicy3.setHeightForWidth(self.playspeedSpinBox.sizePolicy().hasHeightForWidth())
        self.playspeedSpinBox.setSizePolicy(sizePolicy3)
        self.playspeedSpinBox.setMinimum(0.100000000000000)
        self.playspeedSpinBox.setMaximum(2.000000000000000)
        self.playspeedSpinBox.setSingleStep(0.100000000000000)
        self.playspeedSpinBox.setValue(1.000000000000000)

        self.horizontalLayout_7.addWidget(self.playspeedSpinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.PlayerControlGroupBox)
        self.label.setObjectName(u"label")
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label)

        self.volumeSpinBox = QSpinBox(self.PlayerControlGroupBox)
        self.volumeSpinBox.setObjectName(u"volumeSpinBox")
        sizePolicy3.setHeightForWidth(self.volumeSpinBox.sizePolicy().hasHeightForWidth())
        self.volumeSpinBox.setSizePolicy(sizePolicy3)
        self.volumeSpinBox.setMinimum(1)
        self.volumeSpinBox.setMaximum(26)
        self.volumeSpinBox.setValue(13)

        self.horizontalLayout_8.addWidget(self.volumeSpinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_9.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.playerhorizontalSlider = QSlider(self.PlayerControlGroupBox)
        self.playerhorizontalSlider.setObjectName(u"playerhorizontalSlider")
        self.playerhorizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_3.addWidget(self.playerhorizontalSlider)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout_6.addWidget(self.PlayerControlGroupBox)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.widget = QWidget(toolWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy7)

        self.verticalLayout_7.addWidget(self.widget)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)


        self.retranslateUi(toolWindow)

        self.tabWidget.setCurrentIndex(1)

        self.playButton.clicked.connect(toolWindow.Play)
        self.ChooseLyricsButton.connect(QtCore.SIGNAL("clicked()"),toolWindow.ChooseLyrics)
        self.ToHiraganaButton.connect(QtCore.SIGNAL("clicked()"),toolWindow.ConvertText)
        self.ToAlphabetButton.connect(QtCore.SIGNAL("clicked()"),toolWindow.SplitText)
        self.playspeedSpinBox.connect(QtCore.SIGNAL("valueChanged(double)"),toolWindow.ChangePlaySpeed)
        self.playerhorizontalSlider.connect(QtCore.SIGNAL("valueChanged(int)"),toolWindow.PlayerSlide)

        QMetaObject.connectSlotsByName(toolWindow)
    # setupUi

    def retranslateUi(self, toolWindow):
        toolWindow.setWindowTitle(QCoreApplication.translate("toolWindow", u"Form", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("toolWindow", u"Navigate Key Input", None))
        self.ChooseLyricsButton.setText(QCoreApplication.translate("toolWindow", u" Choose Lyrics File ", None))
        self.ToHiraganaButton.setText(QCoreApplication.translate("toolWindow", u" To Hiragana", None))
        self.ToAlphabetButton.setText(QCoreApplication.translate("toolWindow", u"To Alphabet", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("toolWindow", u"Edit Lyrics Text", None))
        self.SelectShapeKeyGroupBox.setTitle(QCoreApplication.translate("toolWindow", u"Select ShapeKeys", None))
        self.label_2.setText(QCoreApplication.translate("toolWindow", u"Character : ", None))
        self.label_4.setText(QCoreApplication.translate("toolWindow", u"shape a : ", None))
        self.label_5.setText(QCoreApplication.translate("toolWindow", u"shape  i : ", None))
        self.label_6.setText(QCoreApplication.translate("toolWindow", u"shape u : ", None))
        self.label_7.setText(QCoreApplication.translate("toolWindow", u"shape e : ", None))
        self.label_8.setText(QCoreApplication.translate("toolWindow", u"shape o : ", None))
        self.checkBox_1.setText(QCoreApplication.translate("toolWindow", u"Selected", None))
        self.checkBox_2.setText(QCoreApplication.translate("toolWindow", u"Selected", None))
        self.checkBox_3.setText(QCoreApplication.translate("toolWindow", u"Selected", None))
        self.checkBox_4.setText(QCoreApplication.translate("toolWindow", u"Selected", None))
        self.checkBox_5.setText(QCoreApplication.translate("toolWindow", u"Selected", None))
        self.PlayerControlGroupBox.setTitle(QCoreApplication.translate("toolWindow", u"Player Control", None))
        self.playButton.setText(QCoreApplication.translate("toolWindow", u"Play", None))
#if QT_CONFIG(shortcut)
        self.playButton.setShortcut(QCoreApplication.translate("toolWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.label_3.setText(QCoreApplication.translate("toolWindow", u"Play Speed :", None))
        self.label.setText(QCoreApplication.translate("toolWindow", u"Volume :", None))
    # retranslateUi

