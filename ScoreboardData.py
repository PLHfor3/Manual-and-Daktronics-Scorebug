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
        self.shotClock = config.defaultShotClockTime1
        self.gameClock = config.defaultGameClockTime
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

    def modifyPeriod(self, value: int) -> None:
        """
        Method to increase/decrease the current period
        :param value: integer value to increase/decrease the period by
        """
        if self.__period + value >= 0:
            self.__period += value

    def getPeriod(self) -> int:
        """
        Method to get the current period
        :return: the current period
        """
        return self.__period

    def setHomeName(self, name: str) -> None:
        """
        Set the Home Team Name
        :param: the name of the home team
        """
        self.__homeTeamName = name

    def setGuestName(self, name: str) -> None:
        """
        Set the Guest Team Name
        :param: the name of the guest team
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
        """
        Toggle whether the home bonus indicator is on or off
        """
        if self.__homeBonus:
            self.__homeBonus = False
        else:
            self.__homeBonus = True

    def setHomeBonus(self, status: bool) -> None:
        """
        Method to set the status of the home bonus indicator
        :param status: boolean value for whether the home bonus indicator is enabled or disabled
        """
        self.__homeBonus = status

    def getHomeBonus(self) -> bool:
        """
        method to get the current home bonus indicator status
        :return: the home bonus status
        """
        return self.__homeBonus

    def toggleGuestBonus(self) -> None:
        """
        Toggle whether the guest bonus indicator is on or off
        """
        if self.__guestBonus:
            self.__guestBonus = False
        else:
            self.__guestBonus = True

    def setGuestBonus(self, status: bool) -> None:
        """
        Method to set the status of the guest bonus indicator
        :param status: boolean value for whether the guest bonus indicator is enabled or disabled
        """
        self.__guestBonus = status

    def getGuestBonus(self) -> bool:
        """
        method to get the current guest bonus indicator status
        :return: the guest bonus status
        """
        return self.__guestBonus

    def modifyHomeScore(self, value) -> None:
        """
        Method to increase or decrease the home score
        :param value: the number to modify the score by
        """
        if self.__homeScore + value >= 0:
            self.__homeScore += value

    def modifyHomeFouls(self, value) -> None:
        """
        Method to increase or decrease the home fouls
        :param value: the number to modify the fouls by
        """
        if self.__homeFouls + value >= 0:
            self.__homeFouls += value

    def getHomeFouls(self) -> int:
        """
        Method to get the current home fouls
        :return: the home fouls
        """
        return self.__homeFouls

    def modifyHomeTOL(self, value) -> None:
        """
        Method to increase or decrease the home timouts left
        :param value: the number to modify the timeouts by
        """
        if self.__homeTOL + value >= 0:
            self.__homeTOL += value

    def getHomeTOL(self) -> int:
        """
        Method to get the current remaining home timeouts
        :return: the home timeouts
        """
        return self.__homeTOL

    def modifyGuestScore(self, value) -> None:
        """
        Method to increase or decrease the guest score
        :param value: the number to modify the score by
        """
        if self.__guestScore + value >= 0:
            self.__guestScore += value

    def modifyGuestFouls(self, value) -> None:
        """
        Method to increase or decrease the guest fouls
        :param value: the number to modify the fouls by
        """
        if self.__guestFouls + value >= 0:
            self.__guestFouls += value

    def getGuestFouls(self) -> int:
        """
        Method to get the current guest fouls
        :return: the guest fouls
        """
        return self.__guestFouls

    def modifyGuestTOL(self, value) -> None:
        """
        Method to increase or decrease the guest timouts left
        :param value: the number to modify the timeouts by
        """
        if self.__guestTOL + value >= 0:
            self.__guestTOL += value

    def getGuestTOL(self) -> int:
        """
        Method to get the current remaining guest timeouts
        :return: the guest timeouts
        """
        return self.__guestTOL
