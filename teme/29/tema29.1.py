# Task 1
# Implement a class Car. Class fields should store the following:
#  model, year of release, manufacturer, engine capacity,
#  color, price. Implement class methods for data input and
#  output, provide access to individual fields through class methods.


class Car:
    def __init__(
        self,
        model="",
        year=0,
        manufacturer="",
        engine_capacity=0.0,
        color="",
        price=0.0,
    ):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    # Method for data input
    def input_data(self):
        self.model = input("Enter car model: ")
        self.year = int(input("Enter year of release: "))
        self.manufacturer = input("Enter manufacturer: ")
        self.engine_capacity = float(input("Enter engine capacity (L): "))
        self.color = input("Enter color: ")
        self.price = float(input("Enter price: "))

    # Method for data output
    def display_data(self):
        print("\nCar Information:")
        print(f"Model: {self.model}")
        print(f"Year of Release: {self.year}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Engine Capacity: {self.engine_capacity} L")
        print(f"Color: {self.color}")
        print(f"Price: ${self.price:,.2f}")

    # Accessor methods (getters)
    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_capacity(self):
        return self.engine_capacity

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    # Mutator methods (setters)
    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_engine_capacity(self, engine_capacity):
        self.engine_capacity = engine_capacity

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price


# Example usage:
if __name__ == "__main__":
    car1 = Car()
    car1.input_data()
    car1.display_data()
