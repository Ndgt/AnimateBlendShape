# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_toolWindow(object):
    def setupUi(self, toolWindow):
        if not toolWindow.objectName():
            toolWindow.setObjectName(u"toolWindow")
        toolWindow.resize(900, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(toolWindow.sizePolicy().hasHeightForWidth())
        toolWindow.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(toolWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(toolWindow)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(toolWindow)
        self.pushButton.clicked.connect(toolWindow.Play)

        QMetaObject.connectSlotsByName(toolWindow)
    # setupUi

    def retranslateUi(self, toolWindow):
        toolWindow.setWindowTitle(QCoreApplication.translate("toolWindow", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("toolWindow", u"PushButton", None))
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("toolWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

