# Task 1
# Add a constructor to the implemented Car class, as well as the required overloaded methods.
# Task 2
# Add a constructor to the implemented Book class, as well as the required overloaded methods.
# Task 3
# Add a constructor to the implemented Stadium class, as well as the required overloaded methods.


from typing import overload


class Car:
    def __init__(self, brand: str, model: str, year: int, price: float):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    @overload
    def display_info(self) -> str: ...

    @overload
    def display_info(self, show_price: bool) -> str: ...

    def display_info(self, show_price: bool = True) -> str:
        info = f"{self.year} {self.brand} {self.model}"
        if show_price:
            info += f" — ${self.price:,.2f}"
        return info

    def get_discounted_price(self, discount: float = 0) -> float:
        """Return price after applying discount percentage."""
        return self.price * (1 - discount / 100)


# Example:
car1 = Car("Toyota", "Corolla", 2021, 20000)
print(car1.display_info())  # Full info with price
print(car1.display_info(False))  # Info without price
print(car1.get_discounted_price(10))  # 10% off
