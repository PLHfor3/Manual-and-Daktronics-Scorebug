import configparser


class Config:

    def __init__(self):
        config = configparser.ConfigParser()
        self.defaultGameClockTime = 480.0
        self.defaultShotClockTime1 = 35
        self.defaultShotClockTime2 = 20
        self.shotTenthOfSecondBelowFive = True
        self.numberOfPeriods = 4
        self.numberOfFoulsForBonus = 5

    def loadConfig(self) -> None:
        pass
