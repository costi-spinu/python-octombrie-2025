# Topic: Inheritance
# Task 1
# Create a Device class containing information about a device.
# Use inheritance to implement a CoffeeMachine class (contains
# info about a coffee machine), a Blender class (contains info
# about a blender), a MeatGrinder class (contains info about a
# meat grinder).
# Each class must have the required methods.

from dataclasses import dataclass, asdict
from typing import Dict


@dataclass
class Device:
    serialnumber: str
    name: str
    year: int
    price: float
    model: str
    number: str

    def creare_dictionar(self) -> Dict:
        return asdict(self)

    @classmethod
    def din_dictionar(cls, d: Dict):
        return cls(
            serialnumber=d["serie numar"],
            name=d["nume produs"],
            year=d["an productie"],
            price=d["pret vanzare"],
            model=d["model"],
            number=d["numar"],
        )


@dataclass
class CoffeeMachine(Device):
    coffee_type: str = "espresso"


@dataclass
class Blender(Device):
    power_watts: int = 600


@dataclass
class MeatGrinder(Device):
    blade_material: str = "steel"


# exemplu rulare
cm = CoffeeMachine(
    serialnumber="CM123",
    name="Philips 2200",
    year=2022,
    price=899.99,
    model="EP2220",
    number="5",
    coffee_type="espresso",
)
print(cm.creare_dictionar())
print(type(cm.creare_dictionar()))
