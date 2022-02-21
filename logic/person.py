class Person(object):
    """
    class used to represent an person
    """

    def __init__(self, id_person: int, name: str = 'name', last_name: str = "Lastname"):
        """person constructor object.

        :param id_person: id of person
        :type id_person: int
        :param name: name of person
        :type name: str
        :param last_name: lastname of person
        :type name: str
        """
        self._id_person = id_person
        self._name = name
        self._last_name = last_name

    @property
    def id_person(self) -> int:
        """ Returns id person of the person.
        :return: id of person.
        :rtype: int
        """
        return self._id_person

    @id_person.setter
    def id_person(self, id_person: int):
        """The id of the person.
        :param id_person: id of person
        :type: int
        """
        self._id_person = id_person

    @property
    def name(self) -> str:
        """ Returns the name of the person.
          :returns: name of person.
          :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """ The name of the person.
        :param name: name of person.
        :type: str
        """
        self._name = name

    @property
    def last_name(self) -> str:
        """ Returns the last name of the person.
          :returns: last name of person.
          :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """ The last name of the person.
        :param last_name: last name of person.
        :type: str
        """
        self._last_name = last_name

    def __str__(self):
        """ Returns str of person
        :return:  string person
        :rtype: str
        """

        return '({0}, {1}, {2})'.format(self._id_person,self._name,self._last_name)


if __name__=='__main__':

    edwin = Person(73577376, "Edwin", "Puertas")
    edwin.name = "Edwin. A"
    print(edwin)