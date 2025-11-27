# Task 1
# Add a constructor to the implemented Car class, as well as the required overloaded methods.


class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def show_info(self, price=2000):
        if price:
            print(f"Am apelat metoda overload si afisez pretul {str(price)} EUR")

        else:
            print(f"{self.year} {self.brand} {self.model}")


# overload
car1 = Car("Dacia", "Logan", 2020, 8500)
car1.show_info()
car1.show_info(5000)
car1.show_info(1000)


# Task 2
# Add a constructor to the implemented Book class, as well as the required overloaded methods.


class Book:
    def __init__(self, title: str = "", year: int = 0, price: int = 0):
        self.title = title
        self.year = year
        self.price = price

    def show_info(self, title: str = ""):
        if title:
            print(f"Titlu carte rescris: {title}")
        else:
            print(f"Titlu: {self.title}, An: {self.year}, Pret: {self.price} lei")


book1 = Book("Fratii Grimm", 1880, 45)

book1.show_info()
book1.show_info("Captain Hook")


# Task 3
# Add a constructor to the implemented Stadium class, as well as the required overloaded methods.


class Stadium:
    def __init__(
        self, name: str = "", city: str = "", capacity: int = 0, opened_year: int = 0
    ):
        self.name = name
        self.city = city
        self.capacity = capacity
        self.opened_year = opened_year

    def show_info(self, capacity: str = ""):
        if capacity:
            print(
                f"Stadion: {self.name}, Oras: {self.city}, An deschidere: {self.opened_year}, Capacitate modificata: {capacity}"
            )
        else:
            print(
                f"Stadion: {self.name}, Oras: {self.city}, An deschidere: {self.opened_year},Capacitate: {self.capacity}"
            )


stadium1 = Stadium("Arena Națională", "București", 55600, 2011)

stadium1.show_info()
stadium1.show_info(234234)
