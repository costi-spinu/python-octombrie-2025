# # Task 1
# # Write a recursive function to find the power of a number.


# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent - 1)
#                 #4*4*4*1

# print(power(4,3))

# # Task 2
# # Write a recursive function that calculates the sum of
# # all numbers in the range from a to b. The user types in
# #  a and b. Illustrate how the function works with an example.

# def recursive_sum(a, b):
#     if a == b:
#         return a
#     return a + recursive_sum(a + 1, b)

# # 1+2+3+4+5

# print (recursive_sum(1,5))


# # Task 3
# Write a recursive function that prints N asterisks in a
# row, N is set by the user. Illustrate how the function
# works with an example.






n=int(input("Da-mi nr:"))
# def func1(a):
#     if a>=0:
#         return print ("*"*a)
    
def func(a):
    if a==0:
        return
    print ("*", end="")
    func(a-1)

func(n)
# # func1(n)

# # Task 4
# # Develop a game of Tic-tac-toe.

# def print_board(board):
#     """Display the Tic-Tac-Toe board"""
#     for row in board:
#         print(" | ".join(row))
#         print("-" * 9)

# def check_winner(board, player):
#     """Check if the player has won"""
#     # Check rows and columns
#     for i in range(3):
#         if all(board[i][j] == player for j in range(3)):
#             return True
#         if all(board[j][i] == player for j in range(3)):
#             return True
#     # Check diagonals
#     if all(board[i][i] == player for i in range(3)):
#         return True
#     if all(board[i][2-i] == player for i in range(3)):
#         return True
#     return False

# def is_full(board):
#     """Check if the board is full (draw)"""
#     return all(cell != " " for row in board for cell in row)

# def tic_tac_toe():
#     """Main game loop"""
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     current_player = "X"

#     while True:
#         print_board(board)
#         print(f"Player {current_player}, enter your move (row and column 1-3):")
#         try:
#             row, col = map(int, input().split())
#             row -= 1
#             col -= 1
#             if row not in range(3) or col not in range(3):
#                 print("Invalid move! Try again.")
#                 continue
#             if board[row][col] != " ":
#                 print("Cell already taken! Try again.")
#                 continue
#         except ValueError:
#             print("Enter two numbers separated by space (e.g., 1 3).")
#             continue

#         board[row][col] = current_player

#         if check_winner(board, current_player):
#             print_board(board)
#             print(f"🎉 Player {current_player} wins!")
#             break

#         if is_full(board):
#             print_board(board)
#             print("It's a draw!")
#             break

#         # Switch player
#         current_player = "O" if current_player == "X" else "X"

# # Run the game
# tic_tac_toe()



# # Task 5
# # Write a recursive function that takes a list of 100
# # random integers and finds the position at which a sequence
# # of 10 numbers begins, and their sum must be the smallest.

# import random

# def gaseste_min_suma(lista, start=0, pozitie_min=0, suma_min=None):
#     # Caz de bază: dacă au rămas mai puțin de 10 numere, ne oprim
#     if start > len(lista) - 10:
#         return pozitie_min, suma_min

#     # Calculăm suma celor 10 numere de la poziția curentă
#     suma_curenta = sum(lista[start:start+10])

#     # Actualizăm dacă am găsit o sumă mai mică
#     if suma_min is None or suma_curenta < suma_min:
#         suma_min = suma_curenta
#         pozitie_min = start

#     # Apel recursiv pentru următoarea poziție
#     return gaseste_min_suma(lista, start + 1, pozitie_min, suma_min)


# # Generăm o listă cu 100 de numere întregi aleatoare între 1 și 50
# numere = [random.randint(1, 50) for _ in range(100)]

# # Apelăm funcția recursivă
# pozitie, suma_min = gaseste_min_suma(numere)

# # Afișăm rezultatele
# print("Lista de numere:", numere)
# print(f"\nCea mai mică sumă ({suma_min}) începe la poziția {pozitie}")
# print("Secvența:", numere[pozitie:pozitie+10])




# # Task 6
# # Write a function that takes two dates (i.e., the function
# #  takes six parameters) and calculates the difference in days
# #  between those dates. To solve this problem, you should also
# # write a function that checks if the year is a leap year.


# # Function to check if a year is a leap year
# def is_leap_year(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# # Number of days in each month for normal and leap years
# days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# def days_since_start_of_year(day, month, year):
#     """Calculate the number of days from Jan 1 to the given date"""
#     total_days = sum(days_in_month[:month-1]) + day
#     if month > 2 and is_leap_year(year):
#         total_days += 1
#     return total_days

# def days_in_year(year):
#     return 366 if is_leap_year(year) else 365

# def date_difference(d1, m1, y1, d2, m2, y2):
#     """Calculate difference in days between two dates"""
#     # If the first date is after the second, swap
#     if (y1, m1, d1) > (y2, m2, d2):
#         d1, m1, y1, d2, m2, y2 = d2, m2, y2, d1, m1, y1

#     # If same year
#     if y1 == y2:
#         return days_since_start_of_year(d2, m2, y2) - days_since_start_of_year(d1, m1, y1)

#     # Days remaining in the first year
#     days = days_in_year(y1) - days_since_start_of_year(d1, m1, y1)

#     # Days in full years in between
#     for year in range(y1+1, y2):
#         days += days_in_year(year)

#     # Days passed in the last year
#     days += days_since_start_of_year(d2, m2, y2)

#     return days

# # Example usage:
# d1, m1, y1 = 15, 2, 2020
# d2, m2, y2 = 25, 3, 2023

# diff = date_difference(d1, m1, y1, d2, m2, y2)
# print(f"The difference between {d1}/{m1}/{y1} and {d2}/{m2}/{y2} is {diff} days.")