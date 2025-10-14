# Task 1

# You have a text file. Create a new file and remove all bad words from it.
# The list of bad words is in another file.

text_raw = "./text_exercitiu.txt"
obscen = "./text_obscur.txt"

# Citim lista de cuvinte obscene
with open(obscen, "r") as f:
    cuv_obscene = [line.strip().lower() for line in f if line.strip()]

# Citim textul sursa
with open(text_raw, "r") as g:
    text = g.read()

# Împărțim textul în cuvinte
cuvinte = text.split()

# Înlocuim cuvintele obscene cu ***
cenzurat = []
for cuv in cuvinte:
    cuv_curat = cuv.lower().strip(".,!?")
    if cuv_curat in cuv_obscene:
        cenzurat.append("***")
    else:
        cenzurat.append(cuv)

# Refacem textul cenzurat
text_cenzurat = " ".join(cenzurat)

# Scriem rezultatul în fișier
with open("./text_cenzurat.txt", "w") as h:
    h.write(text_cenzurat)

print("Cuvintele obscene au fost înlocuite cu '***' în fișierul 'text_cenzurat.txt'.")


# Task 2

# Write a Russian-English transliteration program. Data for transliteration
# are taken from a file and written to another file. The direction is chosen
# by the user through a menu.


# Task 3

# The user enters file names until he or she enters the word "quit." After
# the input completes, the program must combine the contents of all files
# listed by the user into one.

with open("fisierr.txt", "a") as file:
    while True:
        a = input("da mi nume fisier")
        if a == "quit":
            break
        else:
            with open(a) as file2:
                var = file2.read().split()
                file.write(var)

# Task 4

# The user enters file names until he or she enters the word "quit." After
# the input completes, the program must write characters present in all
# listed files to the final file (each file must contain characters).
