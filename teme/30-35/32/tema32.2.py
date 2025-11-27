# Task 2
# Create a Ship class containing information about a ship.
# Use inheritance to implement a Frigate class
# (contains info about a frigate), a Destroyer class
# (contains info about a destroyer), a Cruiser class
# (contains info about a cruiser).
# Each class must have the required methods.


from dataclasses import dataclass, asdict
from typing import Dict


@dataclass
class Nava:
    putere: str
    model: str
    an_fabricatie: int
    pret: float
    tara: str
    culoare: str

    def in_dictionar(self) -> Dict:

        return asdict(self)

    @classmethod
    def din_dictionar(cls, d: Dict):

        return cls(**d)


@dataclass
class Fregata(Nava):
    membri: int
    tunuri: int
    avioane: int
    capacitate: float
    drone: int


@dataclass
class Distrugator(Nava):
    propulsie_nucleara: bool
    numar_rachete: int


@dataclass
class Crucisator(Nava):
    grosime_blindaj: float
    sistem_rachete: str
    raza_radar: float


f = Fregata(
    putere="Diesel",
    model="F-100",
    an_fabricatie=2010,
    pret=150_000_000,
    tara="SUA",
    culoare="Gri",
    membri=200,
    tunuri=10,
    avioane=1,
    capacitate=3000.5,
    drone=4,
)

print("Obiect ca dicționar:")
print(f.in_dictionar())

print("\nReconstruire din dicționar:")
f2 = Fregata.din_dictionar(f.in_dictionar())
print(f2)
