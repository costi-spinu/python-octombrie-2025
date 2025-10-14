# Task 2
# Create an app English-French Dictionary. Store a word in English and
# its French translation. Provide the possibility to add, delete, search,
# and replace data. Use a dictionary to store information.

vocabular = {}


def add_word():
    eng = input("Adauga cuvant in engleza:").strip()
    if not eng:
        print("cuvantul trebuie sa aiba minim o litera")
        return
    french = input(f"Adauga traducerea cuvantului {eng} in franceza:").strip()
    if not french:
        print("cuvantul trebuie sa aiba minim o litera")
        return
    vocabular[eng] = french
    print("Dictionarul creat:", vocabular)


def del_word(cuv):
    if cuv in vocabular:
        del vocabular[cuv]
        print(f"cuvantul {cuv} a fost eliminat")
        print("Dictionar modificat:", vocabular)
    else:
        print("Cuvantul nu exista")
        return print("Dictionarul nu a fost modificat:", vocabular)


def search_word(cuv):
    if cuv in vocabular:
        t = vocabular[cuv]
        print("cuvantul introduse de dumneavoastra exista!")
        print(f"{cuv} = {t}")
    else:
        print(f"{cuv} nu exista in dictionar.")


def replace_word(cuv, cuv_nou):
    if cuv in vocabular:
        french = vocabular[cuv]
        del vocabular[cuv]
        vocabular[cuv_nou] = french
        print(f"Cuvantul {cuv} a fost inlocuit cu {cuv_nou} care inseamna {french}")
        print("Dictionarul nou creat:", vocabular)
    else:
        return print("Cuvantul nu exista")


def replace_value(eng):
    if eng in vocabular:
        valoarea_noua = input("introdu noua traducere:")
        vocabular[eng] = valoarea_noua
        print(f"Pentru cuvantul {eng} s-a introdus noua traducere {valoarea_noua}")
        print(vocabular)
    else:
        print("Nu exista nicio traducere pentru acest cuvant.")


try:
    while True:
        print("Selecteaza (1-5)")
        print("1. Adauga cuvinte in dictionar:")
        print("2. Sterge cuvinte din dictionar:")
        print("3. Cauta cuvinte in dictionar:")
        print("4. Inlocuieste cuvinte din dictionar:")
        print("5. Inlocuieste o traducere:")
        print("6. Iesire!")
        choice = int(input("Selectia dumneavoastra:"))
        if choice == 1:
            add_word()
            continue
        elif choice == 2:
            del_word(cuv=input("Introdu cuvantul pe care doresti sa il elimini:"))
            continue
        elif choice == 3:
            search_word(cuv=input("cautare:"))
            continue
        elif choice == 4:
            replace_word(
                cuv=input("ce doresti sa inlocuiesti:"),
                cuv_nou=input("cuvantul nou introdus: "),
            )
        elif choice == 5:
            replace_value(
                eng=input("Introdu cuvantul caruia vrei sa ii schimbi traducerea:")
            )
        elif choice == 6:
            print("La revedere!")
            break
except ValueError:
    print("Va rugam introduceti un numar de la 1-5.")
