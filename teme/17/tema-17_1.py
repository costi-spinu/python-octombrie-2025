# Task 1
# Create an app that stores information about great basketball players.
# Store the player's full name and height. Provide the possibility to add,
# delete, search, and replace data. Use a dictionary to store information.


#########codurile

jucatori = {}


def adauga_jucator():
    while True:
        nume_jucator = input("Adauga numele jucatorului: ").strip()
        if not nume_jucator:
            print("Numele nu poate fi gol!")
            continue
        try:
            inaltime = float(input("Adauga inaltime jucator: "))
        except ValueError:
            print("Inaltimea trebuie sa fie un numar!")
            continue

        jucatori[nume_jucator] = inaltime
        print(f"Jucatorul {nume_jucator} cu inaltimea {inaltime} a fost adaugat.")
        return print("Dictionar creat", jucatori)


def sterge_jucator(nume_jucator):
    if nume_jucator in jucatori:
        del jucatori[nume_jucator]
        print(f"Jucatorul {nume_jucator} a fost sters.")
        print("Actualizare dictionar:\n\t", jucatori)
    else:
        print(f"Jucatorul {nume_jucator} nu exista in lista.")
    return jucatori


def cauta_jucator(nume_jucator):
    if nume_jucator in jucatori:
        i = jucatori[nume_jucator]
        print(f"numele jucatorului a fost identificat cu inaltimea:{i}")
    else:
        print("Numele jucatorului nu a putut fi identificat:")


def inlocuieste_jucator(nume_jucator, nume_nou):
    if nume_jucator in jucatori:
        inaltime = jucatori[nume_jucator]
        del jucatori[nume_jucator]
        jucatori[nume_nou] = inaltime
        print(f"Numele {nume_jucator} a fost inlocuit cu {nume_nou}")

    else:
        print("Numele jucatorului nu a putut fi identificat:")
    return print("Actualizare dictionar:\n\t", jucatori)


######### programul
try:
    while True:
        print("Selectati(1-5)")
        print("1. Adauga jucator:")
        print("2. Cauta jucator:")
        print("3. Sterge jucator:")
        print("4. Inlocuieste un jucator:")
        print("5. Iesire:")
        choice = int(input("Selectia dumneavoastra:"))
        if choice == 1:
            adauga_jucator()
            continue
        elif choice == 2:
            cauta_jucator(
                nume_jucator=input(
                    "Scrie numele jucatorului pe care doresti sa il cauti:"
                )
            )
            continue
        elif choice == 3:
            sterge_jucator(
                nume_jucator=input(
                    "Scrie numele jucatorului pe care doresti sa il elimini:"
                )
            )
            continue
        elif choice == 4:
            inlocuieste_jucator(
                nume_jucator=input("introdu nume care doresti sa fie inlocuit:\n"),
                nume_nou=input("introdu nume nou:\n"),
            )
            continue
        elif choice == 5:
            print("La revedere!")
        exit()

except ValueError:
    print("Eroare introducere selectie")
