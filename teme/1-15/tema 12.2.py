# #Task 2
# #The user types in text followed by a list of reserved words.
# #Find all reserved words in the text and change lowercase to uppercase there.
# #Print the modified text.

# text exemplu:  Un text este un șir de simboluri sau caractere dintr-un sistem de scriere organizate în propoziții ale unei limbi naturale.
print("Task 2:")
try:
    text = input("Enter text:\n\t")
    while True:
        print(
            "\t1.For changing words in text and make them uppercase \n\t2.Searching words if they are in text:\n\t3.Exit"
        )
        choice = int(input("Choice from 1-3: "))
        if choice == 1:
            print("Text:", text)
            rText = input(
                "Write the words wich you want to reserve and make them uppercase(separated by space)\n\t:"
            )
            reserved_text = rText.split()
            for word in reserved_text:
                text = text.replace(word, word.upper())
            print("Modified text:\n", text)
        elif choice == 2:
            print("Text:", text)
            search = input("Enter the words you want to search:\n\t")
            if search in text:
                numWords = text.count(search)
                print(f" Yes there are {numWords} number(s), in text.")
            else:
                print("There is no such word in text")
        elif choice == 3:
            print("Goodbye:")
            break

except ValueError:
    print("Vallue error!")
