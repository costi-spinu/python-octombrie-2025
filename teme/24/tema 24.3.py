# Task 3
# You have a text file. Delete the last line from it. Write the result to another file.


source_file = "./file1.txt"
output_file = "./file1Rescris.txt"


with open(source_file, "r") as f:
    lines = f.readlines()


if lines:
    lines = lines[:-1]

if lines:
    removed_line = lines.pop()
    print(f"Removed line: {removed_line.strip()}")

with open(output_file, "w") as f:
    f.writelines(lines)

print(f"Last line removed. Updated file written to {output_file}")
