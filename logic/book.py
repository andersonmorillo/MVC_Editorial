from logic.person import Person
from datetime import date

class Book(Person):
    """
    class used to represent the book
    """

    def __init__(self, title: str, id_person: int , name: str, last_name:str, post_date: date, id_book: int, edition: int, no_page: int):
        """book constructor object
        
        :param title: Book's tittle
        :type: str
        :param author: The Book's authors
        :type: object
        :param post_date: Book release date
        :type: object
        :param id_book: Book id
        :type: int 
        :param edition: The book edition
        :type: int
        :param no_page: The number of pages in the book
        :type: int
        """
        Person.__init__(self, id_person, name, last_name)

        self._title = title
        self._post_date = post_date
        self._id_book = id_book
        self._edition = edition
        self._no_page = no_page


    @property
    def title(self) -> str:
        """ Returns the book's title
        :return: Book's tittle
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """ book's title
        :param title: book's title
        :return: str
        """
        self._title = title


    @property
    def post_date(self) -> str:
        """created date of register
        :param: created date of register
        :return: str
        """
        return self._post_date

    @post_date.setter
    def post_date(self, post_date: str):
        """created date of register
        :param post_date: register date
        :type: str
        """
        self._post_date = post_date

    @property
    def id_book(self) -> int:
        """
        :param:
        :return:
        """
        return self._id_book

    @id_book.setter
    def id_book(self, id_book: int):
        """
        :param id_book:
        :return:
        """
        self._id_book = id_book

    @property
    def edition(self) -> int:
        """
        :param:
        :return:
        """
        return self._edition

    @edition.setter
    def edition(self, edition: int):
        """
        :param:
        :type:
        """
        self._edition = edition

    @property
    def no_page(self) -> int:
        """
        :param:
        :return:
        """
        return self._no_page

    @no_page.setter
    def no_page(self, no_page: int):
        """
        :param:
        :type:
        """
        self._no_page = no_page

    def __str__(self):
        """ Returns str of person
        :return:  string person
        :rtype: str
        """

        return '({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7})'.format( self._title, self._id_person, self._name, self._last_name, self._post_date, self.id_book, self._edition,  self._no_page)


if __name__ == '__main__':
    edwin = Person(73577376, "Edwin", "Puertas")
    name = Book("elprincipe",73577376, "Edwin", "Puertas",date.today(),213214,3,321)
    print(name)
    print(edwin)