# Task 2
# Implement a class Book. Class fields should store the following:
# title, year of release, publisher, genre, author, price. Implement
# class methods for data input and output, provide access to individual
# fields through class methods.


class Book:
    def __init__(self, title="", year=0, publisher="", genre="", author="", price=0.0):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    # Method for data input
    def input_data(self):
        self.title = input("Enter book title: ")
        self.year = int(input("Enter year of release: "))
        self.publisher = input("Enter publisher: ")
        self.genre = input("Enter genre: ")
        self.author = input("Enter author: ")
        self.price = float(input("Enter price: "))

    # Method for data output
    def display_data(self):
        print("\nBook Information:")
        print(f"Title: {self.title}")
        print(f"Year of Release: {self.year}")
        print(f"Publisher: {self.publisher}")
        print(f"Genre: {self.genre}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:,.2f}")

    # Accessor methods (getters)
    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    # Mutator methods (setters)
    def set_title(self, title):
        self.title = title

    def set_year(self, year):
        self.year = year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_genre(self, genre):
        self.genre = genre

    def set_author(self, author):
        self.author = author

    def set_price(self, price):
        self.price = price


# Example usage:
if __name__ == "__main__":
    book1 = Book()
    book1.input_data()
    book1.display_data()
