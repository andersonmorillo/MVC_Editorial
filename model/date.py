from time import ctime

time: str = ctime()


class Date(object):
    """
    Class is used for representing the time
    """

    def __init__(self, date: str = 'time'):
        """time constructor object

        :param date: date
        :type date: str
        """

    @property
    def date(self) -> str :
        """Return a specifict date
        :return: time
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date: str):
        """a specifict date

        :param date: date
        :return: str
        """
        self._date = date

    def __str__(self):
        """return str of date

        :return: string date
        :rtype: str
        """

        return '({0})'






