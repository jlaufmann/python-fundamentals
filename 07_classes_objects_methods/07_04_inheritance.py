'''
CLASSES AND INHERITANCE
=======================

1) Define an empty Movie class.

2) Add a dunder init method that takes two arguments "year" and "title"

3) Create a sub-class called "RomCom" that inherits from the Movie class

4) Create another sub-class of the Movie class called "ActionMovie"
    that overwrites the dunder init method of Movie and adds another
    instance variable called "pg" that is set by default to the number 13.

5) EXTRA: If you finish early, use the time to practice flushing out these
    classes and white-boarding code. What attributes could a Movie class
    contain? What methods? What tricks can you use through inheritance?
    Any class attributes you could add?

'''

class Movie:
    """ movie objects with title and year info"""
    def __init__(self, year, title):
        self.year = year
        self.title = title

    def __str__(self):
        return f"{self.title} - {self.year}"


class RomCom(Movie):
    """ RomCom subclass with same characteristics as Movie class"""
    def __init__(self, year, title):
        super().__init__(year, title)


class ActionMovie(Movie):
    """ Action Movie subclass, with an age rating """
    def __init__(self, year, title, pg = 13):
        super().__init__(year, title)
        self.pg = pg


movie1 = Movie(1981, 'The birth of Jim')
movie2 = RomCom(1986, 'When Bob arrived')
movie3 = ActionMovie(2019, 'When Mum moved out', 15)
print(movie1)
print(movie2)
print(movie3)
