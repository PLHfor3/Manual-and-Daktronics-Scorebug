from ManualControllerLogic import *
from ScoreboardData import *
from ScorebugLogic import *
from config import Config


def main():
    config = Config()
    scoreboardData: ScoreboardData = ScoreboardData(config)
    application = QApplication([])
    scorebugWindow = ScorebugLogic()
    scorebugWindow.show()
    controllerWindow = ManualControllerLogic(scoreboardData, scorebugWindow)
    controllerWindow.show()
    application.exec()


if __name__ == '__main__':
    main()
