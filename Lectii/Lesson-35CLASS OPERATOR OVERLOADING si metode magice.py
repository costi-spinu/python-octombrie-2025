class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def showInfo(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Pages: {}".format(self.pages))


book1 = Book("Python Crash Course", "Eric Matthes", 624)
book2 = Book("JavaScript: The Good Parts", "Douglas Crockford", 170)


# numereAdunate = 1 + 1
# concatenareNumere = "1" + "1"

# print(numereAdunate)
# print(concatenareNumere)

# print(type(numereAdunate))
# print(type(concatenareNumere))

# print(type(book1))
# print(type(book2))

# print(book1 + book2) - nu functioneaza pentru ca nu stie sa adune doua clase

#################   METODE MAGICE  #######################
# __add__ - metoda magica
# __init__()
# __new__()


class Class1:
    def __new__(cls):
        print("Hi! I am __new__ magic method.")
        return super(Class1, cls).__new__(cls)

    def __init__(self):
        print("Hi! I am __init__ magic method.")


# __str__() - metoda magica pentru printarea obiectului


# obj1 = Class1()
# print(obj1)


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}, author: {self.author}, pages: {self.pages}"

    def __eq__(self, otherObj):
        if self.author == otherObj.author and self.title == otherObj.title:
            return True
        else:
            return False

    def __gt__(self, otherObj):
        if self.pages > otherObj.pages:
            return True
        else:
            return False


book1 = Book("Python Crash Course", "Eric Matthes", 624)
book2 = Book("JavaScript: The Good Parts", "Douglas Crockford", 170)
book3 = Book("JavaScript: The Good Parts", "Douglas Crockford", 170)
book4 = book3
print(book1)
print(book1.__str__())
print(book2.__str__())
print(book1 == book2)  # False fara constructor __eq_/__gt__ -> False
print(book2 == book3)  # False fara constructor __eq_ /__gt__-> True
print(book3 == book4)  # True fara constructor __eq_ /__gt__-> True


# TABEL
# __eq__           == equal
# __ne__           != not equal
# __lt__            < mai mic less than
# __le__           <= mai mic sau egal  less than equal
# __gt__            > mai mare greater than
# __ge__           >= mai mare sau egal greater than equal
