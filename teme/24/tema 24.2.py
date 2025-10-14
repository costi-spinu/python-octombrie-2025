# Task 2
# You have a text file. Create a new file and write the following statistics based on the source file to it:
# Number of characters;
# Number of lines;
# Number of vowels;
# Number of consonants;
# Number of digits.


# File names
source_file = "./file1.txt"
output_file = "./fisierRescris.txt"

# Initialize counters
num_chars = 0
num_lines = 0
num_vowels = 0
num_consonants = 0
num_digits = 0

# Define vowels
vowels = "aeiouAEIOU"

# Open the source file and calculate statistics
with open(source_file, "r") as file:
    for line in file:
        num_lines += 1
        num_chars += len(line)
        for char in line:
            if char.isdigit():
                num_digits += 1
            elif char.isalpha():
                if char in vowels:
                    num_vowels += 1
                else:
                    num_consonants += 1

# Write the statistics to the output file
with open(output_file, "w") as file:
    file.write(f"Number of characters: {num_chars}\n")
    file.write(f"Number of lines: {num_lines}\n")
    file.write(f"Number of vowels: {num_vowels}\n")
    file.write(f"Number of consonants: {num_consonants}\n")
    file.write(f"Number of digits: {num_digits}\n")

n = (
    f"Number of characters: {num_chars}",
    f"Number of characters: {num_chars}",
    f"Number of lines: {num_lines}",
    f"Number of consonants: {num_consonants}",
    f"Number of digits: {num_digits}",
)

print(f"Statistics {n} written to {output_file}")
