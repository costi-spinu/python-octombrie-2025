# Task 1
# Add a static method to the Fraction class that when called returns
# the number of created Fraction class objects.
class Fraction:
    _count = 0  # static variable to track created instances

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction._count += 1

    @staticmethod
    def get_instance_count():
        return Fraction._count


# Task 2
# Create a class to convert temperature from Celsius to Fahrenheit,
# and vice versa. The class must have two static methods: to convert
# from Celsius to Fahrenheit and from Fahrenheit to Celsius. The class
#  should also count how many times the temperature was calculated and
# return this value using a static method.


class TemperatureConverter:
    _count = 0

    @staticmethod
    def c_to_f(celsius):
        TemperatureConverter._count += 1
        return (celsius * 9 / 5) + 32

    @staticmethod
    def f_to_c(fahrenheit):
        TemperatureConverter._count += 1
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def get_calculation_count():
        return TemperatureConverter._count


# Task 3
# Create a class to convert from metric to imperial, and vice versa.
#  Implement this functionality as static methods. Be sure to implement
# a converter for units of length.


class UnitConverter:

    # --- Metric to Imperial ---
    @staticmethod
    def meters_to_feet(meters):
        return meters * 3.28084

    @staticmethod
    def meters_to_inches(meters):
        return meters * 39.3701

    @staticmethod
    def kilometers_to_miles(km):
        return km * 0.621371

    # --- Imperial to Metric ---
    @staticmethod
    def feet_to_meters(feet):
        return feet * 0.3048

    @staticmethod
    def inches_to_meters(inches):
        return inches * 0.0254

    @staticmethod
    def miles_to_kilometers(miles):
        return miles * 1.60934


print("Task 3")
print(UnitConverter.meters_to_feet(1))
print(UnitConverter.kilometers_to_miles(5))
print(UnitConverter.miles_to_kilometers(10))

print("Task 2")

print(TemperatureConverter.c_to_f(0))
print(TemperatureConverter.f_to_c(212))
print(TemperatureConverter.get_calculation_count())

print("Task 1")
f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
print(Fraction.get_instance_count())
