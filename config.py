import configparser


class Config:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        self.defaultGameClockTime = float(config['game options']['defaultGameClockTime'])
        self.defaultShotClockTime1 = float(config['game options']['defaultShotClockTime1'])
        self.defaultShotClockTime2 = float(config['game options']['defaultShotClockTime2'])
        if config['game options']['shotTenthOfSecondBelowFive'] == "True":
            self.shotTenthOfSecondBelowFive = True
        else:
            self.shotTenthOfSecondBelowFive = False
        self.numberOfPeriods = int(config['game options']['numberOfPeriods'])
        self.numberOfFoulsForBonus = int(config['game options']['numberOfFoulsForBonus'])

    def loadConfig(self) -> None:
        self.__init__()
