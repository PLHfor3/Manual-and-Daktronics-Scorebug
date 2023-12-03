from PyQt6.QtWidgets import *

from ScorebugGUI import *


class ScorebugLogic(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setContentsMargins(0, 0, 0, 0)
        # self.button_submit.clicked.connect(lambda: self.print_output())
        # self.button_10.clicked.connect(lambda: self.update_tip_percent("10"))
        # self.button_15.clicked.connect(lambda: self.update_tip_percent("15"))
        # self.button_20.clicked.connect(lambda: self.update_tip_percent("20"))
        # self.button_clear.clicked.connect(lambda: self.clear_all())
