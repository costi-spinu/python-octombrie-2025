# Task 1
# The user types in an arithmetic expression. For example, 23+12.
# Print its result. In our example, the output is 35. The arithmetic
# expression can have only three parts: number, op, number.
# Possible operations: +, -, *, /.

print("Task 1")
import re  # importam pentru split si strip

op = input("Enter an arithmetic expression with 2 numbers: ")
numbers = re.split(r"[+\-*/]", op)
numbers = [
    s.strip() for s in numbers if s.strip()
]  # eliminăm spațiile goale si transformam in lista
print(f"Numbers in the expression: {numbers}")
num1 = float(numbers[0])  # extragere numar 1 din lista pozitia 0
num2 = float(numbers[1])  # extragere numar 2 din lista pozitia 1

if len(numbers) != 2:  # ne asiguram ca avem doua numere
    print("Error!")
else:
    if "+" in op:
        result = num1 + num2
    elif "-" in op:
        result = num1 - num2
    elif "*" in op:
        result = num1 * num2
    elif "/" in op:
        result = num1 / num2
    print(op, "=", result)
