# # Task 1
# # The user types in a number. Determine how many digits this number has,
# # find their sum and average. Determine how many zeros this number has. Implement a dialog with the user through a menu.
while True:
    number = input("Pleaae provide a number, or type 'quit' to leave: ")
    if number == "quit":
        print("bye")
        break
    if not number.isdigit():
        print("Please provide a valid input.")
        continue
    number_count = len(number)
    print(f"The number has {number_count} digits")
    zero_counter = 0

    number_list = []

    for num in number:
        number_list.append(int(num))
        # When you do number_list.append(int(num)),
        #  you convert that string to an int only for the append,
        #  but num itself remains a string because you never reassigned it.
        total = sum(number_list)
        average = total / number_count
        num = int(num)
        if num == 0:
            zero_counter = zero_counter + 1
    print(f"The number of zeros in the number is {zero_counter}")

    print(f"The total sum of the digits of your number is {total}")
    print(f"The average sum of the digits within your number is: {average}")
    # print(number_list[0])
    print("Would you like to try again?")
    choice = input("Type 'again', or 'stop'.")

    if choice == "stop":
        print("bye")
        break
    if choice == "again":
        continue


# Task 2
# Write a program that displays a chessboard with a set cell size. For example, three,
# ***---***---***---***---
# ***---***---***---***---
# ***---***---***---***---
# ---***---***---***---***
# ---***---***---***---***
# ---***---***---***---***

# size = int(input("Type the size: "))
# # for _ in range(size):
# #     print(("*" + "_") * size)
# User inputs
cell_size = int(input("Enter the cell size (e.g., 3): "))
border_size = int(input("Enter the border size (e.g., 2): "))

board_size = 8  # 8x8 chessboard

total_width = board_size * cell_size + 2 * border_size
total_height = board_size * cell_size + 2 * border_size

for row in range(total_height):
    line_str = ""
    for col in range(total_width):
        # Check if we are in the border area
        if (
            row < border_size
            or row >= total_height - border_size
            or col < border_size
            or col >= total_width - border_size
        ):
            # Print border character, for example '#'
            line_str += "#"
        else:
            # Inside the chessboard area:
            # Adjust coordinates relative to the chessboard start
            board_row = (row - border_size) // cell_size
            board_col = (col - border_size) // cell_size

            # Decide cell color based on parity
            if (board_row + board_col) % 2 == 0:
                line_str += "*"
            else:
                line_str += "-"
    print(line_str)


# Task 3
# Write a program that tests users for their multiplication table skills.
# The program prints two numbers, and the user must enter their product.
# Develop several levels of difficulty (they should differ in complexity and number of questions).
#  Print the points that represent the user's skills.

# questions = [(2, 3), (4, 5), (1, 1), (5, 5), (3, 4)]

# score = 0
# total = len(questions)

# for i in range(total):
#     a, b = questions[i]
#     answer = input(f"Question {i+1}: What is {a} * {b}? ")

#     if not answer.isdigit():
#         print("Invalid input. Counting as wrong.")
#         continue

#     if int(answer) == a * b:
#         print("Correct!")
#         score += 1
#     else:
#         print(f"Wrong. The correct answer is {a * b}.")

# print(f"\nYou scored {score} out of {total} points.")
# percentage = score / total * 100
# print(f"Your skill level: {percentage:.1f}% correct.")


# or


# import random

# print("Test de tabla înmulțirii")
# print("1 - Ușor   (1-5, 5 întrebări)")
# print("2 - Mediu  (1-10, 7 întrebări)")
# print("3 - Greu   (5-15, 10 întrebări)")

# nivel = input("Alege nivelul: ")

# if nivel == "1":
#     a_min, a_max, q = 1, 5, 5
# elif nivel == "2":
#     a_min, a_max, q = 1, 10, 7
# elif nivel == "3":
#     a_min, a_max, q = 5, 15, 10
# else:
#     print("Nivel invalid. Setat pe Ușor.")
#     a_min, a_max, q = 1, 5, 5

# puncte = 0

# for i in range(q):
#     x = random.randint(a_min, a_max)
#     y = random.randint(a_min, a_max)
#     rasp = int(input(f"{x} × {y} = "))
#     if rasp == x * y:
#         puncte += 1

# print(f"Scor final: {puncte}/{q}")

# if puncte == q:
#     print("🏆 Maestru!")
# elif puncte >= q * 0.8:
#     print("💪 Foarte bine!")
# elif puncte >= q * 0.5:
#     print("🙂 Acceptabil")
# else:
#     print("📚 Mai mult exercițiu")


# or


print("Multiplication Table Skills Test")
print("Select difficulty level:")
print("1 - Easy (numbers 1 to 5, 5 questions)")
print("2 - Medium (numbers 1 to 10, 10 questions)")
print("3 - Hard (numbers 1 to 12, 15 questions)")

level = input("Enter level (1-3): ")

if level == "1":
    max_num = 5
    questions = 5
elif level == "2":
    max_num = 10
    questions = 10
elif level == "3":
    max_num = 12
    questions = 15
else:
    print("Invalid level. Exiting.")
    exit()

# Create a list of all multiplication pairs
pairs = []
for i in range(1, max_num + 1):
    for j in range(1, max_num + 1):
        pairs.append((i, j))

# Pseudo-random number generator variables
seed = 7
n = len(pairs)

# Shuffle pairs list using Fisher-Yates and inline pseudo-random logic
for i in range(n - 1, 0, -1):
    # Generate pseudo-random index j
    seed = (seed * 9301 + 49297) % 233280
    j = seed % (i + 1)
    # Swap pairs[i] and pairs[j]
    pairs[i], pairs[j] = pairs[j], pairs[i]

score = 0

# Ask the questions
for q in range(questions):
    a, b = pairs[q]
    correct = a * b
    answer = input(f"Question {q + 1}: What is {a} * {b}? ")

    if not answer.isdigit():
        print("Invalid input. Counting as wrong answer.")
        continue

    if int(answer) == correct:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. The correct answer is {correct}.")

print(f"\nYou scored {score} out of {questions} points.")
percentage = (score / questions) * 100
print(f"Your skill level: {percentage:.1f}% correct.")


# Task 4
# Print a rhombus made out of asterisks.
n = int(input("Introdu n (ex: 3 sau 5): "))

for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))





