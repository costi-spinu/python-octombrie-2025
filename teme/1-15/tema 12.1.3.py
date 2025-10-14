# Task 1
# The user types in a string. Check if this string is a palindrome.
# A palindrome is a word or text that reads the same backward as forward.
# For instance, racecar; "Do geese see God?"; tenet; "Was it a car or a cat I saw?"
# #
# #"^"      Matches the start of the string.
# # []       Indicates a set of characters.
# #\A       Matches only at the start of the string.
# #\Z       Matches only at the end of the string.
# #'[^A-Za-z0-9] - alfabetic litere mari si mici, numeric 0-9

print("Task 1:")
import re

text = input("Enter the text for checking if is a palindrome:")
checking = re.sub(r"[^A-Za-z0-9]", "", text).lower()
if checking == checking[::-1]:
    print("Yes, text is a palindrome:\n\t", text)
    print("Result is: \n\t", checking)
else:
    print("No,text is not a palindrome")


# #Task 3
# #There is some text. Count the number of sentences in it and print the result.
# #Text exemplu: Hello! How are you? I hope you are fine.
print("Task 3:")

## varianta 1
import re

text = input("Copy text, or write one:")
sentences = re.split(r"[.?!]", text)
sentences = [s for s in sentences if s.strip()]  # strip - eliminare spatii goale
print(f"There are {len(sentences)} sentences:")

## varianta 2
num_sentences = text.count(".") + text.count("?") + text.count("!")
print((f"There are {num_sentences} sentences:"))
