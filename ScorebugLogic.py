from PyQt6.QtWidgets import *

from ScorebugGUI import *


class ScorebugLogic(QMainWindow, Ui_ScoreBug):

    def __init__(self) -> None:
        """
        Initialize ScoreBug
        """
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setContentsMargins(0, 0, 0, 0)

    def mousePressEvent(self, event) -> None:
        """
        Method to help move frameless window when interacted with from the mouse
        """
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event) -> None:
        """
        Method to help move frameless window when interacted with from the mouse
        """
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()
