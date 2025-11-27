# Task 1
# Use multiple inheritance to develop a class
# Circle Inscribed in a Square.


import math


class Square:
    def __init__(self, side):
        self.side = side  # side length of the square

    def area(self):
        return self.side**2

    def perimeter(self):
        return 4 * self.side


class Circle:
    def __init__(self, radius):
        self.radius = radius  # radius of the circle

    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return 2 * math.pi * self.radius


class CircleInscribedInSquare(Square, Circle):
    def __init__(self, side):
        # First, initialize the Square part
        Square.__init__(self, side)
        # For an inscribed circle, radius = side / 2
        Circle.__init__(self, side / 2)

    def show_dimensions(self):
        print(f"Square side: {self.side}")
        print(f"Circle radius (inscribed): {self.radius}")


# Example usage:
cis = CircleInscribedInSquare(10)

cis.show_dimensions()
print("Square area:", cis.area())  # From Square (MRO: Square.area)
print("Square perimeter:", cis.perimeter())
print("Circle area:", Circle.area(cis))  # Explicitly calling Circle.area
print("Circle circumference:", cis.circumference())


# Task 2
# Use multiple inheritance to develop a class Car.
# There should also be these classes: Wheels, Engine, Doors, etc.


class Wheels:
    def __init__(self, wheel_count=4):
        self.wheel_count = wheel_count

    def rotate(self):
        return f"No of wheels {self.wheel_count}"


class Engine:
    def __init__(self, horsepower=100):
        self.horsepower = horsepower

    def start_engine(self):
        return f"Engine started with {self.horsepower} HP."


class Doors:
    def __init__(self, door_count=4):
        self.door_count = door_count

    def open_doors(self):
        return f"{self.door_count} doors"


# Car inherits from multiple classes
class Car(Wheels, Engine, Doors):
    def __init__(
        self,
        wheel_count=4,
        horsepower=100,
        door_count=4,
        brand="Dacia",
        model="Sandero",
    ):
        Wheels.__init__(self, wheel_count)
        Engine.__init__(self, horsepower)
        Doors.__init__(self, door_count)
        self.brand = brand
        self.model = model

    def show_specs(self):
        return (
            f"Car Brand: {self.brand}\n"
            f"Car Model: {self.model}\n"
            f"Wheels: {self.wheel_count}\n"
            f"Engine: {self.horsepower} HP\n"
            f"Doors: {self.door_count}"
        )


car = Car(4, 90, 5, "Dacia", "Sandero")
print(car.start_engine())
print(car.rotate())
print(car.open_doors())
print(car.show_specs())


# Task 3
# Create a base class Pet and derived classes Dog,
# Cat, Parrot, Hamster. Use a constructor to set the
# name of each animal and its characteristics.
#  Implement the following methods for each class:
# Sound — makes the sound of an animal (type in the console);
# Show — shows the name of an animal;
# Type — shows the name of its subspecies.

# Task 4
# Create a base class Employer with the Print() function.
# It should print info about the employer. In the case of a
#  base class, it can be a string that reads: This is Employer class.
# Create three derived classes: President, Manager, Worker.
# Override the Print() function to output information appropriate
#  for each type of employer.

# Task 5
# Implement the magic method str and int (to return the age of the employer)
# for the classes from Task 4.
