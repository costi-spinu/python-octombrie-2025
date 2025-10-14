import random

rand_num = random.randint(1, 100)
nr_incercari = 7
print("Welcome to Guess the Number")
print("Remaining attempts (", nr_incercari, ")\n")

inp_num = int(input("Your number is: "))

for x in range(1, 7):
    if inp_num == rand_num:
        print("Congratulations, you guessed the number. ", inp_num)
        break
    else:
        nr_incercari -= 1
        print("Remaining attempts (", nr_incercari, ")")
        inp_num = int(input("Your number is: "))
        continue
if nr_incercari == 1:
    print("You've exhausted all attempts, maybe next time you'll be lucky.")
