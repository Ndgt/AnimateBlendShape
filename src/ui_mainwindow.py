# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QTabWidget, QTableView, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 400)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, -1, 10, 5)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tableView = QTableView(self.tab)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 10, 371, 291))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_6.addWidget(self.tabWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_6.addItem(self.verticalSpacer)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.SelectShapeKeyGroupBox = QGroupBox(self.centralwidget)
        self.SelectShapeKeyGroupBox.setObjectName(u"SelectShapeKeyGroupBox")
        self.SelectShapeKeyGroupBox.setFlat(False)
        self.verticalLayout_4 = QVBoxLayout(self.SelectShapeKeyGroupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_2 = QLabel(self.SelectShapeKeyGroupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.SelectShapeKeyGroupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.lineEdit)

        self.selectModelButton = QToolButton(self.SelectShapeKeyGroupBox)
        self.selectModelButton.setObjectName(u"selectModelButton")

        self.horizontalLayout_10.addWidget(self.selectModelButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = QComboBox(self.SelectShapeKeyGroupBox)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.comboBox)

        self.checkBox = QCheckBox(self.SelectShapeKeyGroupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setTristate(False)

        self.horizontalLayout.addWidget(self.checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox_2 = QComboBox(self.SelectShapeKeyGroupBox)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy2.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.comboBox_2)

        self.checkBox_2 = QCheckBox(self.SelectShapeKeyGroupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_2.addWidget(self.checkBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.comboBox_3 = QComboBox(self.SelectShapeKeyGroupBox)
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy2.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.comboBox_3)

        self.checkBox_3 = QCheckBox(self.SelectShapeKeyGroupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_3.addWidget(self.checkBox_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBox_4 = QComboBox(self.SelectShapeKeyGroupBox)
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy2.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.comboBox_4)

        self.checkBox_4 = QCheckBox(self.SelectShapeKeyGroupBox)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_4.addWidget(self.checkBox_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.comboBox_5 = QComboBox(self.SelectShapeKeyGroupBox)
        self.comboBox_5.setObjectName(u"comboBox_5")
        sizePolicy2.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.comboBox_5)

        self.checkBox_5 = QCheckBox(self.SelectShapeKeyGroupBox)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.horizontalLayout_5.addWidget(self.checkBox_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.verticalLayout_6.addWidget(self.SelectShapeKeyGroupBox)

        self.PlayerControlGroupBox = QGroupBox(self.centralwidget)
        self.PlayerControlGroupBox.setObjectName(u"PlayerControlGroupBox")
        self.PlayerControlGroupBox.setFlat(False)
        self.PlayerControlGroupBox.setCheckable(False)
        self.verticalLayout_5 = QVBoxLayout(self.PlayerControlGroupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.playButton = QPushButton(self.PlayerControlGroupBox)
        self.playButton.setObjectName(u"playButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())
        self.playButton.setSizePolicy(sizePolicy3)
#if QT_CONFIG(shortcut)
        self.playButton.setShortcut(u"Ctrl+S")
#endif // QT_CONFIG(shortcut)

        self.horizontalLayout_9.addWidget(self.playButton)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.PlayerControlGroupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.playspeedSpinBox = QDoubleSpinBox(self.PlayerControlGroupBox)
        self.playspeedSpinBox.setObjectName(u"playspeedSpinBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.playspeedSpinBox.sizePolicy().hasHeightForWidth())
        self.playspeedSpinBox.setSizePolicy(sizePolicy4)
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
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label)

        self.volumeSpinBox = QSpinBox(self.PlayerControlGroupBox)
        self.volumeSpinBox.setObjectName(u"volumeSpinBox")
        sizePolicy4.setHeightForWidth(self.volumeSpinBox.sizePolicy().hasHeightForWidth())
        self.volumeSpinBox.setSizePolicy(sizePolicy4)
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


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 33))
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy5)
        self.menubar.setMaximumSize(QSize(16777215, 50))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setGeometry(QRect(330, 289, 149, 50))
        sizePolicy3.setHeightForWidth(self.menuFile.sizePolicy().hasHeightForWidth())
        self.menuFile.setSizePolicy(sizePolicy3)
        self.menuFile.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(9)
        self.menuFile.setFont(font)
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Navigate Key Input", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Edit Lyrics Text", None))
        self.SelectShapeKeyGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Select ShapeKeys", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Model path", None))
        self.selectModelButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Selected", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Selected", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Selected", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Selected", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Selected", None))
        self.PlayerControlGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Player Control", None))
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Play Speed :", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Volume :", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

