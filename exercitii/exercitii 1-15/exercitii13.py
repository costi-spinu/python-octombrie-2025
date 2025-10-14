# # Task 1
# # There is some text. Implement the following features:
# # Change the text so that each sentence starts with a capital letter;
# # Count how many times numbers appear in the text;
# # Count how many times punctuation marks appear in the text;
# # Count the number of exclamation marks in the text.


print("Task1")
text = input("Insert text:")
# Change the text so that each sentence starts with a capital letter;
print(text.title())
# Count how many times numbers appear in the text;
numbers = sum(c.isdigit() for c in text)
print(numbers)
# Count how many times punctuation marks appear in the text;
import string

punctuation = sum(c in string.punctuation for c in text)
print(punctuation)
# Count the number of exclamation marks in the text.
exclametion = text.count("!")
print(exclametion)

# # Task 2
# # The user types in a list of integers and a number. Count how many times
# # this number appears in the list. Print the result.

# print("Task2")
# numbers = list(int, input("Enter a list of integers (separated by spaces): ").split())
# target = int(input("Enter the number to count: "))
# count = numbers.count(target)
# print(f"The number {target} appears {count} time(s) in the list.")


# ##SEBE CRISTIAN
# # # lista_nr = []

# # input_lista = input("Introdu o lista de numere intregi: ")
# # numar_de_cautat = int(input("Introdu un numar intreg pe care sa il caut in lista: "))

# # elemente_text = input_lista.split()

# # for element in elemente_text:
# #     numar = int(element)
# #     lista_nr.append(numar)

# # contor_numar = 0

# # for i in range(len(lista_nr)):
# #     if lista_nr[i] == numar_de_cautat:
# #         contor_numar = contor_numar + 1

# # print("Am regasit numarul " + str(numar_de_cautat) + " de " + str(contor_numar) + " ori.")


# # Task 3
# # The user types in a list of integers. Calculate the sum
# # and average of these elements. Print the result.

print("Task3")
# numbers = list(
#     map(int, input("Enter a list of integers (separated by spaces): ").split())
# )

numbers = list(
    map(int, input("Enter a list of integers (separated by spaces): ").split())
)

total = sum(numbers)
average = total / len(numbers) if numbers else 0  # avoid division by zero
print("Sum:", total)
print("Average:", average)
