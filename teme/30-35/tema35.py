# Topic: Decorators.
# Task 1
# Create a function that returns a list with all prime numbers from 0 to 1000.
# Use decorators to count how many seconds it takes to find all prime numbers.
#  Print the time and prime numbers.


import time


# --- Decorator to measure execution time ---
def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Time taken: {end - start:.6f} seconds")
        return result

    return wrapper


# --- Function to generate primes from 0 to 1000 ---
@timer
def get_primes():
    primes = []
    for num in range(2, 1001):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


# --- Run it ---
prime_numbers = get_primes()
print("Prime numbers from 0 to 1000:")
print(prime_numbers)


# timer decorator:
# Records the start and end time.
# Prints out the number of seconds the function took.
# get_primes():
# Loops from 2 to 1000.
# Checks if each number is prime.
# Returns a list of all primes.


# Task 2
# Supplement Task 1 with the ability to pass the start and end points of the
# range to search for all prime numbers.

import time


# --- Decorator that works with any parameters ---
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start:.6f} seconds")
        return result

    return wrapper


# --- Prime number function with start & end parameters ---
@timer
def get_primes(start_num, end_num):
    primes = []
    for num in range(start_num, end_num + 1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


# --- Run it with any range you want ---
prime_numbers = get_primes(0, 1000)  # Example usage from Task 1
print("Prime numbers:")
print(prime_numbers)


# Task 3
# Your company submits financial statements to various government agencies
#  every year. The reporting formats differ from organization to organization.
# Use decorators to solve this problem.


# Funcția de bază: creează situația financiară într-un format intern
def situatie_financiara(an):
    return {
        "an": an,
        "firma": "ACME SRL",
        "venituri": 1500000,
        "cheltuieli": 900000,
        "profit": 1500000 - 900000,
        "moneda": "EUR",
    }


# --- Decoratori pentru formate diferite ---


# Decorator pentru ANAF (ex: format tip CSV simplu)
def format_anaf(func):
    def wrapper(an):
        data = func(an)
        linie = f'{data["an"]},{data["firma"]},{data["venituri"]},{data["cheltuieli"]},{data["profit"]},{data["moneda"]}'
        return "AN,COMPANIE,VENITURI,CHELTUIELI,PROFIT,MONEDA\n" + linie

    return wrapper


# Decorator pentru Institutul de Statistica (ex: format text mai descriptiv)
def format_statistica(func):
    def wrapper(an):
        data = func(an)
        return (
            f"Raport Statistica pentru anul {data['an']}\n"
            f"Firma: {data['firma']}\n"
            f"Venituri: {data['venituri']} {data['moneda']}\n"
            f"Cheltuieli: {data['cheltuieli']} {data['moneda']}\n"
            f"Profit: {data['profit']} {data['moneda']}\n"
        )

    return wrapper


# --- Funcții „specializate” pentru fiecare instituție ---


@format_anaf
def raport_anaf(an):
    return situatie_financiara(an)


@format_statistica
def raport_statistica(an):
    return situatie_financiara(an)


# --- Exemplu de folosire ---

an = 2024

print("=== Raport pentru ANAF ===")
print(raport_anaf(an))
print()

print("=== Raport pentru Institutul de Statistica ===")
print(raport_statistica(an))
