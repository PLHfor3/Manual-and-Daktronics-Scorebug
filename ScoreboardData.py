from config import Config


class ScoreboardData:
    def __init__(self, config: Config):
        """
        Initialize Default Scoreboard Values
        :param config: default scoreboard configuration container
        """
        self.configuration = config
        self.__homeScore = 0
        self.__guestScore = 0
        self.__homeTOL = 4
        self.__guestTOL = 4
        self.__homeFouls = 0
        self.__guestFouls = 0
        self.shotClock = 0.0
        self.gameClock = 4800.0
        self.__period = 1
        self.__homeTeamName = "Home"
        self.__guestTeamName = "Guest"
        self.__homeBonus = False
        self.__guestBonus = False

    def getHomeScore(self) -> int:
        """
        get the current home score
        :return: the current home score
        """
        return self.__homeScore

    def getGuestScore(self) -> int:
        """
        get the current guest score
        :return: the current guest score
        """
        return self.__guestScore

    def modifyPeriod(self, value) -> None:
        self.__period += value

    def setHomeName(self, name) -> None:
        """
        Set the Home Team Name
        :return:
        """
        self.__homeTeamName = name

    def setGuestName(self, name) -> None:
        """
        Set the Guest Team Name
        :return:
        """
        self.__guestTeamName = name

    def getHomeName(self) -> str:
        """
        Get Home team name
        :return: the home team name
        """
        return self.__homeTeamName

    def getGuestName(self) -> str:
        """
        Get Guest team name
        :return: the guest team name
        """
        return self.__guestTeamName

    def toggleHomeBonus(self) -> None:
        if self.__homeBonus:
            self.__homeBonus = False
        else:
            self.__homeBonus = True

    def setHomeBonus(self, status: bool) -> None:
        self.__homeBonus = status

    def getHomeBonus(self) -> bool:
        return self.__homeBonus

    def toggleGuestBonus(self) -> None:
        if self.__guestBonus:
            self.__guestBonus = False
        else:
            self.__guestBonus = True

    def setGuestBonus(self, status: bool) -> None:
        self.__guestBonus = status

    def getGuestBonus(self) -> bool:
        return self.__guestBonus

    def modifyHomeScore(self, value) -> None:
        self.__homeScore += value

    def modifyHomeFouls(self, value) -> None:
        self.__homeFouls += value

    def getHomeFouls(self) -> int:
        return self.__homeFouls

    def modifyHomeTOL(self, value) -> None:
        self.__homeTOL += value

    def getHomeTOL(self) -> int:
        return self.__homeTOL

    def modifyGuestScore(self, value) -> None:
        self.__guestScore += value

    def modifyGuestFouls(self, value) -> None:
        self.__guestFouls += value

    def getGuestFouls(self) -> int:
        return self.__guestFouls

    def modifyGuestTOL(self, value) -> None:
        self.__guestTOL += value

    def getGuestTOL(self) -> int:
        return self.__guestTOL
