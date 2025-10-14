import time


def joaca_jocul():
    timp_limitat = 31
    incercari_max = 10
    incercari = 0
    start = time.time()

    numere_corecte = [2, 4, 7, 15, 20, 23, 37, 85, 94, 56, 13, 68, 41, 64, 28, 87, 90]

    while incercari < incercari_max:
        timp_curent = time.time()
        timp_ramas = timp_limitat - (timp_curent - start)

        if timp_ramas <= 0:
            print("Timpul s-a scurs! Ai pierdut!")
            break

        print("Timp rămas: {} secunde".format(int(timp_ramas)))

        try:
            numar = int(input("Alege un număr de la 1 la 100: "))
            incercari += 1

            if numar in numere_corecte:
                print("Ai ghicit, felicitări!")
                break
            else:
                print("Nu ai ghicit, mai încearcă.\n")

        except ValueError:
            print("Te rog să introduci un număr valid")

    else:
        print("Ai epuizat numărul maxim de încercări. Mai încearcă data viitoare!")


while True:
    joaca_jocul()

    raspuns = input("Vrei să rejoci? (da/nu): ").strip().lower()
    if raspuns == "da":
        print("Se reîncepe jocul în:")
        for sec in range(5, 0, -1):
            print(sec)
            time.sleep(1)
        print("\nReîncepem!")
    else:
        print("Mulțumesc pentru joc! La revedere!")
        break
