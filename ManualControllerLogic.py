import time

from PyQt6.QtWidgets import *

from ManualControllerGUI import *
from ScoreboardData import ScoreboardData
from ScorebugLogic import ScorebugLogic


class ManualControllerLogic(QMainWindow, Ui_MainWindow):

    def __init__(self, scoreboardData: ScoreboardData, scorebugWindow: ScorebugLogic):
        super().__init__()
        self.scorebugWindow = scorebugWindow
        self.setupUi(self)
        self.__scoreboardData = scoreboardData
        self.updateScoreBug()
        self.homeScore1.clicked.connect(lambda: self.__scoreboardData.modifyHomeScore(1))
        self.homeScore1.clicked.connect(lambda: self.updateScoreBug())
        self.homeScore2.clicked.connect(lambda: self.__scoreboardData.modifyHomeScore(2))
        self.homeScore2.clicked.connect(lambda: self.updateScoreBug())
        self.homeScore3.clicked.connect(lambda: self.__scoreboardData.modifyHomeScore(3))
        self.homeScore3.clicked.connect(lambda: self.updateScoreBug())
        self.homeScoreMinus.clicked.connect(lambda: self.__scoreboardData.modifyHomeScore(-1))
        self.homeScoreMinus.clicked.connect(lambda: self.updateScoreBug())
        self.homeTeamName.textChanged.connect(lambda: self.__scoreboardData.setHomeName(self.homeTeamName.text()))
        self.homeTeamName.textChanged.connect(lambda: self.updateScoreBug())
        self.homeFoulsPlus.clicked.connect(lambda: self.__scoreboardData.modifyHomeFouls(1))
        self.homeFoulsMinus.clicked.connect(lambda: self.__scoreboardData.modifyHomeFouls(-1))
        self.homeFoulsPlus.clicked.connect(lambda: self.updateScoreBug())
        self.homeFoulsMinus.clicked.connect(lambda: self.updateScoreBug())
        self.homeTOLPlus.clicked.connect(lambda: self.__scoreboardData.modifyHomeTOL(1))
        self.homeTOLPlus.clicked.connect(lambda: self.updateScoreBug())
        self.homeTOLMinus.clicked.connect(lambda: self.__scoreboardData.modifyHomeTOL(-1))
        self.homeTOLMinus.clicked.connect(lambda: self.updateScoreBug())

        self.guestScore1.clicked.connect(lambda: self.__scoreboardData.modifyGuestScore(1))
        self.guestScore1.clicked.connect(lambda: self.updateScoreBug())
        self.guestScore2.clicked.connect(lambda: self.__scoreboardData.modifyGuestScore(2))
        self.guestScore2.clicked.connect(lambda: self.updateScoreBug())
        self.guestScore3.clicked.connect(lambda: self.__scoreboardData.modifyGuestScore(3))
        self.guestScore3.clicked.connect(lambda: self.updateScoreBug())
        self.guestScoreMinus.clicked.connect(lambda: self.__scoreboardData.modifyGuestScore(-1))
        self.guestScoreMinus.clicked.connect(lambda: self.updateScoreBug())
        self.guestTeamName.textChanged.connect(lambda: self.__scoreboardData.setGuestName(self.guestTeamName.text()))
        self.guestTeamName.textChanged.connect(lambda: self.updateScoreBug())
        self.guestFoulsPlus.clicked.connect(lambda: self.__scoreboardData.modifyGuestFouls(1))
        self.guestFoulsMinus.clicked.connect(lambda: self.__scoreboardData.modifyGuestFouls(-1))
        self.guestFoulsPlus.clicked.connect(lambda: self.updateScoreBug())
        self.guestFoulsMinus.clicked.connect(lambda: self.updateScoreBug())
        self.guestTOLPlus.clicked.connect(lambda: self.__scoreboardData.modifyGuestTOL(1))
        self.guestTOLPlus.clicked.connect(lambda: self.updateScoreBug())
        self.guestTOLMinus.clicked.connect(lambda: self.__scoreboardData.modifyGuestTOL(-1))
        self.guestTOLMinus.clicked.connect(lambda: self.updateScoreBug())
        self.periodPlus.clicked.connect(lambda: self.__scoreboardData.modifyPeriod(1))
        self.periodPlus.clicked.connect(lambda: self.updateScoreBug())

        self.periodMinus.clicked.connect(lambda: self.__scoreboardData.modifyPeriod(-1))
        self.periodMinus.clicked.connect(lambda: self.updateScoreBug())

        self.gameClockisRunning = False
        self.gameClockTimeAtStart = 0.0
        self.gameClockTimer = QtCore.QTimer(self)
        self.gameClockTimer.timeout.connect(self.updateGameClock)
        self.toggleMainClock.clicked.connect(lambda: self.toggleGameClock())

        self.shotClockisRunning = False
        self.shotClockTimeAtStart = 0.0

    def toggleGameClock(self):
        if self.gameClockisRunning:
            currentTime = time.time()
            self.gameClockisRunning = False
            self.__scoreboardData.gameClock -= (
                    currentTime - self.gameClockTimeAtStart)  # TODO THINK ABOUT GETTERS AND SETTERS FOR CLOCK
            self.scorebugWindow.mainClock.setText(f"{self.__scoreboardData.gameClock}")
            self.gameClockTimer.stop()
        else:
            self.gameClockisRunning = True
            self.gameClockTimeAtStart = time.time()
            self.gameClockTimer.start(10)

    def updateGameClock(self):
        currentTime = time.time()
        self.scorebugWindow.mainClock.setText(
            self.formatGameTime(self.__scoreboardData.gameClock - (currentTime - self.gameClockTimeAtStart)))

    def formatGameTime(self, seconds: float) -> str:
        if seconds < 60.0:
            if seconds < 10.0:
                return f"0{seconds:.1f}"
            else:
                return f"{seconds:.1f}"
        elif seconds < 600.0:
            minutes = seconds / 60

    def formatShotTime(self, seconds: float) -> str:
        if seconds < 5.0 and self.__scoreboardData.configuration.shotTenthOfSecondBelowFive:
            return f""

    def updateScoreBug(self):
        self.scorebugWindow.homeScore.setText(f"{self.__scoreboardData.getHomeScore()}")
        self.scorebugWindow.guestScore.setText(f"{self.__scoreboardData.getGuestScore()}")
        self.scorebugWindow.homeName.setText(f"{self.__scoreboardData.getHomeName()}")
        self.scorebugWindow.guestName.setText(f"{self.__scoreboardData.getGuestName()}")
        self.scorebugWindow.homeFouls.setText(f"Fouls: {self.__scoreboardData.getHomeFouls()}")
        self.scorebugWindow.guestFouls.setText(f"Fouls: {self.__scoreboardData.getGuestFouls()}")
        self.scorebugWindow.homeTOL.setText(f"Timeouts: {self.__scoreboardData.getHomeTOL()}")
        self.scorebugWindow.guestTOL.setText(f"Timeouts: {self.__scoreboardData.getGuestTOL()}")
        if self.__scoreboardData.getHomeFouls() >= self.__scoreboardData.configuration.numberOfFoulsForBonus:
            self.__scoreboardData.setGuestBonus(True)
        else:
            self.__scoreboardData.setGuestBonus(False)
        if self.__scoreboardData.getHomeBonus():
            self.scorebugWindow.homeBonus.setHidden(False)
        else:
            self.scorebugWindow.homeBonus.setHidden(True)
        if self.__scoreboardData.getGuestBonus():
            self.scorebugWindow.guestBonus.setHidden(False)
        else:
            self.scorebugWindow.guestBonus.setHidden(True)

    def closeEvent(self, *args, **kwargs):
        super(QtGui.QMainWindow, self).closeEvent(*args, **kwargs)
        self.scorebugWindow.close()
