# Task 5
# You have a text file. Count how many times the word specified by the user occurs in it.

source_file = "./file1.txt"

word = input("Enter the word to count: ")
try:

    with open(source_file, "r", encoding="utf-8") as file:
        text = file.read()

    #
    count = text.lower().split().count(word.lower())

    print(f"The word '{word}' occurs {count} times in the file.")
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
