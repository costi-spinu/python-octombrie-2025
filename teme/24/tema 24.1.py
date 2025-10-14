# Task 1
# You have two text files. Find out if their lines match. If they don't, print the mismatched line from each file.


def compare_files(file1, file2):
    # deschidem fișierele în mod citire
    with open(file1, "r") as f1, open(file2, "r") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # aflăm lungimea minimă
    min_len = min(len(lines1), len(lines2))

    # comparăm linie cu linie
    for i in range(min_len):
        if lines1[i].strip() != lines2[i].strip():
            print(f"Line {i+1} mismatch:")
            print(f"  {file1}: {lines1[i].strip()}")
            print(f"  {file2}: {lines2[i].strip()}")

    # verificăm dacă unul are linii în plus
    if len(lines1) > len(lines2):
        print(f"\nExtra lines in {file1}:")
        for i in range(min_len, len(lines1)):
            print(f"  Line {i+1}: {lines1[i].strip()}")

    elif len(lines2) > len(lines1):
        print(f"\nExtra lines in {file2}:")
        for i in range(min_len, len(lines2)):
            print(f"  Line {i+1}: {lines2[i].strip()}")


# exemplu de apel
compare_files("file1.txt", "file2.txt")
