# # Task 1
# # The user types in a string. Rotate the strings and display the result.

mystring = input("What is the string: ")
print(mystring[::-1])

# # Task 2
# # The user types in a string. Count the number of letters and digits in the string.
# # Print both results.


string2 = input("\nTask 2 - Enter a string: ")
letters = sum(c.isalpha() for c in string2)
digits = sum(c.isdigit() for c in string2)
print("Letters:", letters)
print("Digits:", digits)

c = 0
d = 0
a = input("da mi str")
if type(a) == str:
    for i in a:
        if i.isdigit():
            d += 1
        if i.isalpha():
            c += 1


# # Task 3
# # The user types in a string and a symbol to be searched for. Count how many times
# # this symbol appears in the string. Print the result.

a = input()
b = input()
c = a.count(b)
print(c)


# # Task 4
# # The user types in a string and a search word. Count how many times this word
# # appears in the string. Print the result.

text = input("Enter a string: ")
word = input("Enter the word to search for: ")
count = text.split().count(word)
print(f"The word '{word}' appears {count} times in the string.")

# # Task 5
# # The user types in a string, a search word, and a replacement word.
# # Replace one word with another one in the string. Print the resulting string.

text = input("Enter a string: ")
search_word = input("Enter the word to search for: ")
replacement_word = input("Enter the replacement word: ")
result = text.replace(search_word, replacement_word)
print("Resulting string:", result)
