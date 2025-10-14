# Task 6
# You have a text file. Find and replace the specified word.
# The user determines what to search for and to what it should be replaced.

source_file = "./file1.txt"
output_file = "./file1Rescris.txt"


word_to_replace = input("Enter the word to find: ")
replacement_word = input("Enter the word to replace it with: ")

try:

    with open(source_file, "r") as f:
        text = f.read()

    updated_text = text.replace(word_to_replace, replacement_word)

    with open(output_file, "w") as f:
        f.write(updated_text)

    print(
        f"All occurrences of '{word_to_replace}' have been replaced with '{replacement_word}'."
    )
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
