import time

from PyQt6.QtWidgets import *

from ManualControllerGUI import *
from ScoreboardData import ScoreboardData
from ScorebugLogic import ScorebugLogic


class ManualControllerLogic(QMainWindow, Ui_ScoreController):

    def __init__(self, scoreboardData: ScoreboardData, scorebugWindow: ScorebugLogic) -> None:
        """
        Intialize the Manual Controller Window and form all connections
        :param scoreboardData: the values containing scoreboard dats such as score and time
        :param scorebugWindow: the window displaying all scoreboard data
        """
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
        self.gameClockTimeAtStart = self.__scoreboardData.gameClock
        self.scorebugWindow.mainClock.setText(self.formatGameTime(self.__scoreboardData.gameClock))
        self.gameClockTimer = QtCore.QTimer(self)
        self.gameClockTimer.timeout.connect(self.updateGameClock)
        self.toggleMainClock.clicked.connect(lambda: self.toggleGameClock())

        self.shotClockisRunning = False
        self.shotClockTimeAtStart = 0.0
        self.scorebugWindow.shotClock.setText(self.formatShotTime(self.__scoreboardData.shotClock))
        self.shotClockTimer = QtCore.QTimer(self)
        self.shotClockTimer.timeout.connect(self.updateShotClock)
        self.toggleShotTimer.clicked.connect(lambda: self.toggleShotClock())

        self.setHomeLogo.clicked.connect(lambda: self.setHomeLogoFunc())
        self.setGuestLogo.clicked.connect(lambda: self.setGuestLogoFunc())

        self.scorebugWindow.homePoss.setHidden(True)
        self.scorebugWindow.guestPoss.setHidden(True)
        self.homePoss.clicked.connect(lambda: self.changeHomePoss())
        self.guestPoss.clicked.connect(lambda: self.changeGuestPoss())
        self.resetMainClock.clicked.connect(lambda: self.resetGameClockFunc())
        self.resetShotTimer1.clicked.connect(lambda: self.resetShotClockFunc1Click())
        self.resetShotTimer2.clicked.connect(lambda: self.resetShotClockFunc2Click())

        self.setMainClock.clicked.connect(lambda: self.setMainClockFunc())
        self.setShotTimer.clicked.connect(lambda: self.setShotClockFunc())

    def setMainClockFunc(self) -> None:
        """
        Method to open a window to set the main clock
        """
        time = self.getTimerValue("Game Clock", "Enter the game clock time in seconds: ")
        if time:
            self.__scoreboardData.gameClock = time
            self.scorebugWindow.mainClock.setText(self.formatGameTime(self.__scoreboardData.gameClock))

    def setShotClockFunc(self) -> None:
        """
        Method to open a window to set the shot clock
        """
        time = self.getTimerValue("Shot Clock", "Enter the shot clock time in seconds: ")
        if time:
            self.__scoreboardData.shotClock = time
            self.scorebugWindow.shotClock.setText(self.formatShotTime(self.__scoreboardData.shotClock))

    def getTimerValue(self, title: str, label: str) -> str or bool:
        """
        Method to open the input dialog window
        :param title: the inout dialog window title
        :param label: the inout dialog window label
        :return: the user's input or False
        """
        text, ok = QInputDialog.getDouble(self, title, label)
        if ok:
            return text
        return False

    def resetGameClockFunc(self) -> None:
        """
        Method to reset the game clock to default config value
        """
        self.__scoreboardData.gameClock = self.__scoreboardData.configuration.defaultGameClockTime
        self.scorebugWindow.mainClock.setText(self.formatGameTime(self.__scoreboardData.gameClock))

    def resetShotClockFunc1Click(self) -> None:
        """
        Method to reset the shot clock to the default configured full length shot clock value
        """
        if self.shotClockisRunning:
            self.toggleShotClock()
            self.__scoreboardData.shotClock = self.__scoreboardData.configuration.defaultShotClockTime1
            self.scorebugWindow.shotClock.setText(self.formatShotTime(self.__scoreboardData.shotClock))
            self.toggleShotClock()
        else:
            self.__scoreboardData.shotClock = self.__scoreboardData.configuration.defaultShotClockTime1
            self.scorebugWindow.shotClock.setText(self.formatShotTime(self.__scoreboardData.shotClock))

    def resetShotClockFunc2Click(self) -> None:
        """
        Method to reset the shot clock to the default configured partial length shot clock value
        """
        if self.shotClockisRunning:
            self.toggleShotClock()
            self.__scoreboardData.shotClock = self.__scoreboardData.configuration.defaultShotClockTime2
            self.scorebugWindow.shotClock.setText(self.formatShotTime(self.__scoreboardData.shotClock))
            self.toggleShotClock()
        else:
            self.__scoreboardData.shotClock = self.__scoreboardData.configuration.defaultShotClockTime2
            self.scorebugWindow.shotClock.setText(self.formatShotTime(self.__scoreboardData.shotClock))

    def changeHomePoss(self) -> None:
        """
        Method to set the possession arrow to the home setting
        """
        self.scorebugWindow.homePoss.setHidden(False)
        self.homePoss.setEnabled(False)
        self.guestPoss.setEnabled(True)
        self.scorebugWindow.guestPoss.setHidden(True)

    def changeGuestPoss(self) -> None:
        """
        Method to set the possession arrow to the guest setting
        """
        self.scorebugWindow.homePoss.setHidden(True)
        self.homePoss.setEnabled(True)
        self.guestPoss.setEnabled(False)
        self.scorebugWindow.guestPoss.setHidden(False)

    def setHomeLogoFunc(self) -> None:
        """
        Method to open a file selector to select the home logo
        """
        filePath = QFileDialog.getOpenFileName(self, "Select Home Team Logo", "", "All Files(*)")
        if filePath:
            self.scorebugWindow.homeLogo.setPixmap(QtGui.QPixmap(filePath[0]))
            self.homeLogo.setPixmap(QtGui.QPixmap(filePath[0]))

    def setGuestLogoFunc(self) -> None:
        """
        Method to open a file selector to select the guest logo
        """
        filePath = QFileDialog.getOpenFileName(self, "Select Guest Team Logo", "", "All Files(*)")
        if filePath:
            self.scorebugWindow.guestLogo.setPixmap(QtGui.QPixmap(filePath[0]))
            self.guestLogo.setPixmap(QtGui.QPixmap(filePath[0]))

    def toggleGameClock(self) -> None:
        """
        Method to toggle the game clock on or off
        """
        if self.gameClockisRunning:
            self.gameClockisRunning = False
            self.scorebugWindow.mainClock.setText(
                self.formatGameTime(
                    self.__scoreboardData.gameClock - (self.currentGameTime - self.gameClockTimeAtStart)))
            self.__scoreboardData.gameClock -= (
                    self.currentGameTime - self.gameClockTimeAtStart)

            self.gameClockTimer.stop()
            self.resetMainClock.setEnabled(True)
            self.setMainClock.setEnabled(True)
        else:
            self.gameClockisRunning = True
            self.gameClockTimeAtStart = time.time()
            self.gameClockTimer.start(10)
            self.resetMainClock.setEnabled(False)
            self.setMainClock.setEnabled(False)

    def updateGameClock(self) -> None:
        """
        Helper method to be run every time the game clock timer object executes to update the game time
        """
        self.currentGameTime = time.time()
        if self.__scoreboardData.gameClock - (self.currentGameTime - self.gameClockTimeAtStart) > 0.0:
            var = self.__scoreboardData.gameClock - (self.currentGameTime - self.gameClockTimeAtStart)
            self.scorebugWindow.mainClock.setText(
                self.formatGameTime(
                    self.__scoreboardData.gameClock - (self.currentGameTime - self.gameClockTimeAtStart)))
        else:
            self.gameClockTimer.stop()
            self.gameClockisRunning = False
            self.resetMainClock.setEnabled(True)
            self.setMainClock.setEnabled(True)
            self.__scoreboardData.gameClock = 0.0

    def formatGameTime(self, seconds: float) -> str:
        """
        Helper method to format the game clock output to be displayed on the scorebug
        :param seconds: the number of seconds remaining in the game
        :return: the string of the correctly formatted game time to be displayed on the scorebug
        """
        if seconds < 60.0:
            return "%04.1f" % seconds
        elif seconds < 600.0:
            minutes = int(seconds / 60)
            minSeconds = int(seconds % 60)
            return f"{minutes:.0f}:{minSeconds:02d}"
        else:
            minutes = int(seconds / 60)
            minSeconds = int(seconds % 60)
            return f"{minutes:02d}:{minSeconds:02d}"

    def toggleShotClock(self) -> None:
        """
        Method to toggle the shot clock on or off
        """
        if self.shotClockisRunning:
            # self.currentTime = time.time()
            self.shotClockisRunning = False
            self.scorebugWindow.shotClock.setText(
                self.formatShotTime(
                    self.__scoreboardData.shotClock - (self.currentShotTime - self.shotClockTimeAtStart)))
            self.__scoreboardData.shotClock -= (
                    self.currentShotTime - self.shotClockTimeAtStart)

            self.shotClockTimer.stop()
            self.setShotTimer.setEnabled(True)
        else:
            self.shotClockisRunning = True
            self.shotClockTimeAtStart = time.time()
            self.shotClockTimer.start(10)
            self.setShotTimer.setEnabled(False)

    def updateShotClock(self) -> None:
        """
        Helper method to be run every time the shot clock timer object executes to update the shot time
        """
        self.currentShotTime = time.time()
        if self.__scoreboardData.shotClock - (self.currentShotTime - self.shotClockTimeAtStart) > 0.0:
            var = self.__scoreboardData.shotClock - (self.currentShotTime - self.shotClockTimeAtStart)
            self.scorebugWindow.shotClock.setText(
                self.formatShotTime(
                    self.__scoreboardData.shotClock - (self.currentShotTime - self.shotClockTimeAtStart)))
        else:
            self.shotClockTimer.stop()
            self.shotClockisRunning = False
            self.setShotTimer.setEnabled(True)
            self.__scoreboardData.shotClock = 0.0

    def formatShotTime(self, seconds: float) -> str:
        """
        Helper method to format the shot clock output to be displayed on the scorebug
        :param seconds: the number of seconds remaining on the shot clock
        :return: the string of the correctly formatted shot time to be displayed on the scorebug
        """
        if seconds < 5.0 and self.__scoreboardData.configuration.shotTenthOfSecondBelowFive:
            return f"{seconds:.1f}"
        else:
            return f"{int(seconds)}"

    def updateScoreBug(self) -> None:
        """
        Method to update all values displayed on the scorebug
        """
        self.scorebugWindow.homeScore.setText(f"{self.__scoreboardData.getHomeScore()}")
        self.scorebugWindow.guestScore.setText(f"{self.__scoreboardData.getGuestScore()}")
        self.scorebugWindow.homeName.setText(f"{self.__scoreboardData.getHomeName()}")
        self.scorebugWindow.guestName.setText(f"{self.__scoreboardData.getGuestName()}")
        self.scorebugWindow.homeFouls.setText(f"Fouls: {self.__scoreboardData.getHomeFouls()}")
        self.scorebugWindow.guestFouls.setText(f"Fouls: {self.__scoreboardData.getGuestFouls()}")
        self.scorebugWindow.homeTOL.setText(f"Timeouts: {self.__scoreboardData.getHomeTOL()}")
        self.scorebugWindow.guestTOL.setText(f"Timeouts: {self.__scoreboardData.getGuestTOL()}")
        self.scorebugWindow.period.setText(f"Per: {self.__scoreboardData.getPeriod()}")

        if self.__scoreboardData.getHomeFouls() >= self.__scoreboardData.configuration.numberOfFoulsForBonus:
            self.__scoreboardData.setGuestBonus(True)
        else:
            self.__scoreboardData.setGuestBonus(False)
        if self.__scoreboardData.getGuestFouls() >= self.__scoreboardData.configuration.numberOfFoulsForBonus:
            self.__scoreboardData.setHomeBonus(True)
        else:
            self.__scoreboardData.setHomeBonus(False)

        if self.__scoreboardData.getHomeBonus():
            self.scorebugWindow.homeBonus.setHidden(False)
        else:
            self.scorebugWindow.homeBonus.setHidden(True)
        if self.__scoreboardData.getGuestBonus():
            self.scorebugWindow.guestBonus.setHidden(False)
        else:
            self.scorebugWindow.guestBonus.setHidden(True)

    def closeEvent(self, *args, **kwargs) -> None:
        """
        Method to help close all windows when the controller window is closed
        """
        super(QtGui.QMainWindow, self).closeEvent(*args, **kwargs)
        self.scorebugWindow.close()
