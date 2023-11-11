class ScoreboardData:
    def __init__(self):
        self.__homeScore = 0
        self.__guestScore = 0
        self.__homeTOL = 0
        self.__guestTOL = 0
        self.__homeFouls = 0
        self.__guestFouls = 0
        self.__shotClock = 0
        self.__gameClock = 0.0
        self.__period = 1
        self.__homeTeamName = "Home"
        self.__guestTeamName = "Guest"
        self.__homeBonus = False
        self.__guestBonus = False
