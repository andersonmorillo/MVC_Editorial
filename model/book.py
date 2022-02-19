from person import Person
from date import Date

person = Person

class Book(Person):
    """
    clase used to represent the book
    """

    def __init__(self, title: str, author: list(Person), post_date: Date, id_book: int, edition: int, no_pag: int):
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
        :param no_pag: The number of pages in the book
        :type: int
        """
        self._title = title
        self._author = author
        self._post_date = post_date
        self._id_book = id_book
        self._edition = edition
        self._no_pag = no_pag

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

