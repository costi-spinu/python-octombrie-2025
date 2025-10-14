import random
import time

optiuni = ["piatra", "hartie", "foarfeca"]

victorii = 0
infrangeri = 0
remize = 0

while True:
    jucator = input("Alege: piatra, hartie sau foarfeca (sau 'exit' ca să ieși): ").lower()

    if jucator == "exit":
        print("La revedere!")
        break

    if jucator not in optiuni:
        print("Opțiune invalidă. Încearcă din nou.")
        continue

    calculator = random.choice(optiuni)
    print("Calculatorul a ales: " + calculator)

    if jucator == calculator:
        print("Egalitate!")
        remize += 1
    elif(jucator == "piatra" and calculator == "foarfeca") or \
         (jucator == "hartie" and calculator == "piatra") or \
         (jucator == "foarfeca" and calculator == "hartie"):
        print("Ai câștigat!")
        victorii +=1
    else:
        print("Ai pierdut!")
        infrangeri += 1

        raspuns = input("Vrei o remiză (reluare runda)? (da/nu): ").lower()
    if raspuns == "da":
        print("Se rejoacă runda...")
        for sec in range(5, 0, -1):
            print(f"Reîncepem în {sec} secunde...", end='\r')
            time.sleep(1)
        print(" " * 30, end='\r')  # curăță linia
        continue
    else:
     print("\nScor final:")
    print("Victorii:", victorii)
    print("Înfrângeri:", infrangeri)
    print("Remize:", remize)
    print("Mulțumesc pentru că ai jucat!")
    break


