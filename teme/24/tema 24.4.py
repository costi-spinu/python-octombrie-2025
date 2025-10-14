# Task 4
# You have a text file. Find the length of the longest line.


source_file = "./file1.txt"

max_length = 0
longest_line = ""

with open(source_file, "r") as file:
    for line in file:
        line_content = line.rstrip("\n")
        line_length = len(line_content)
        if line_length > max_length:
            max_length = line_length
            longest_line = line_content

print(f"The length of the longest line is: {max_length}")
print(f"The longest line is: '{longest_line}'")
