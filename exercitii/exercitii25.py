# # Task 1

# # You have a text file. Create a new file where you should write
# # all words consisting of at least seven letters found in the source file.


# with open("text.txt") as f:
#     text = f.read().split()
#     for i in text:
#         if len(i) > 7:
#             with open("newfile.txt", "w") as g:
#                 g.write(i)

# # Task 2

# # You have a text file. Write its lines to another file.
# # The order of lines in the second file must match the order
# # of lines in the source file.

# with open("text.txt") as g:
#     g.seek(0, 2)
#     end = g.tell()
#     g.seek(0)
#     with open("secondfile.txt", "w") as j:
#         while True:
#             pos = g.tell()
#             if pos != end:
#                 line = g.readline()
#                 j.write(line)
#             else:
#                 break


# Task 3

# You have a text file. Write its lines to another file.
# The order of lines in the second file must be inverse.


# with open("text.txt", "r", encoding="utf-8") as g:
#     lines = g.readlines()

# with open("secondfile.txt", "w", encoding="utf-8") as j:
#     for line in reversed(lines):
#         j.write(line)


# Task 4

# You have a text file. Add a line consisting of twelve
# asterisks (************) after the last line among the
# lines that have no comma. If there are no such lines in
# the file, the asterisks should be added after all lines
# of the existing file. Write the result to another file.


# Task 5

# You have a text file. Calculate the number of words
# that begin with a character set by the user.

# char = input("da-mi caracter: ")
# c = 0
# with open("text.txt") as f:
#     var = f.read().split()
#     for i in var:
#         if char == 1:
#             c += 1
# print(c)


# Task 6

# You have a text file. Write all its lines to another
# file while replacing * with & and vice versa.

# with open("text.txt") as f, open("secondfile.txt") as g:
#     for line in f:
#         swapped = line.replace("*", "#").replace("&", "*").replace("#", "&")
#         g.write(swapped)

# Task 7

# You have an array of strings. Write them to a file
# while placing each array element on a separate line and preserving the order.

# Task 8

# You have an array of strings. Write them to a file
# while placing each array element on a separate line and reversing the order.

# Task 9

# You have a text file. Calculate the number of characters in it.

# Task 10

# You have a text file. Calculate the number of lines in it.
