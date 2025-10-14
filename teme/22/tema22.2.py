# Task 2
# Implement the first assignment through a function.
# The function must take name and age as parameters
#  and return a formatted string. The correctness
# check of the data received must be inside the function.
# Create two versions of the function implementation:
# The first version does not handle the exception inside
# the function. All processing is outside the function;
# The second version handles the exception inside the function.


print("Varianta 1")


def welcome_user(name, age):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Numele a fost introdus gresit")
    if not isinstance(age, int) or age < 0 or age > 130:
        raise ValueError("Varsta trebuie sa fie intre 0-130")
    return f"Hello {name}! Varsta ta este {age} ani."


try:
    name = input("name:")
    age = int(input("age:"))
    print(welcome_user(name, age))

except ValueError as e:
    print(f"Error:{e}")

print("Varianta 2")


def welcome_user2(name, age):
    try:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Numele a fost introdus gresit")
        if not isinstance(age, int) or age < 0 or age > 130:
            raise ValueError("Varsta trebuie sa fie intre 0-130")
        return f"Hello {name}! Varsta ta este {age} ani."
    except ValueError as e:
        return f"Invalid input: {e}"


try:
    name = input("name:")
    age = int(input("age:"))
    print(welcome_user2(name, age))

except ValueError as e:
    print(f"Error:{e}")
