from pyfbsdk import*
from pyfbsdk_additions import*

try:
    from PySide6 import QtWidgets
except:
    from PySide2 import QtWidgets

from ui_mainwidget import Ui_toolWindow

class HoldedWidget(QtWidgets.QWidget, Ui_toolWindow):
    def __init__(self, pwidholder):
        super().__init__(pwidholder)
        self.setupUi(self)

