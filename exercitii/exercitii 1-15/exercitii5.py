# Task 1
# The user types in the time in seconds since the beginning of the day.
# Based on the user's choice, calculate how many hours,
# minutes, and seconds are left until midnight.


# print("\n--- Task 1 ---")
# seconds_since_day_start = int(
#     input("Enter the number of seconds since the beginning of the day: ")
# )
# total_seconds_in_day = 86400  # 24 * 60 * 60

# if 0 <= seconds_since_day_start <= total_seconds_in_day:
#     seconds_left = total_seconds_in_day - seconds_since_day_start
#     hours = seconds_left // 3600
#     minutes = (seconds_left % 3600) // 60
#     seconds = seconds_left % 60
#     print(f"Time left until midnight: {hours}h {minutes}m {seconds}s")
# else:
#     print("Invalid input: number of seconds must be between 0 and 86400.")


# Task 2
# The user types in the diameter of a circle.
# Based on the user's choice, calculate the area or perimeter of the circle


# print("\n--- Task 2 ---")
# diameter = float(input("Enter the diameter of the circle: "))
# choice = (
#     input("Type 'area' to calculate area or 'perimeter' to calculate perimeter: ")
#     .strip()
#     .lower()
# )
# radius = diameter / 2

# if choice == "area":
#     area = 3.14 * radius**2
#     print(f"Area of the circle: {area:.2f}")
# elif choice == "perimeter":
#     perimeter = 3.14 * diameter
#     print(f"Perimeter (circumference) of the circle: {perimeter:.2f}")
# else:
#     print("Invalid choice.")

# Task 3
# The user types in the cost of one gaming console, their quantity,
# and a discount. Based on the user's choice,
# calculate the total amount of the order or the cost of one console,
# including the discount.

try:
    while True:
        cost = float(input("introdu pret consola:"))
        quantity = int(input("introdu numar bucati:"))
        discount = float(input("introdu discount pret:"))
        print(
            "Ce doriti sa calculati?\n1.Pret total comanda cu discount.\n2.Pret o singura consola cu discount.\n3.Pret total comanda fara discount."
        )

        choice = int(input("Selectati (1/3):"))
        if choice == 1:
            result1 = cost * quantity * (discount / 100)
            result2 = (cost * quantity) - result1
            print("Pret total comanda cu discount este de:", result2)
        elif choice == 2:
            result1 = cost * (discount / 100)
            result2 = cost - result1
            print("Pret o singur consola cu discount este:", result2)

        elif choice == 3:
            print(cost * quantity)
        else:
            print("invalid error")
        while True:
            again = input("\n Doresti sa incerci alte preturi?(y/n):").strip().lower()
            if again == "y":
                break
            elif again == "n":
                print("See you!")
                exit()
            elif again == "exit":
                print("bye bye!!!")
                exit()
            else:
                print("Invalid input, Please type'y' or 'exit' for yes or 'n' for no")

except ValueError:
    print("eroare!")


# Task 4
# The user types in the file size in gigabytes and the bandwidth in bits per second.
# Based on the user's choice, calculate how many hours, or minutes,
# or seconds it will take to download a file.

# Get user input
file_size_gb = float(input("Enter the file size in gigabytes (GB): "))
bandwidth_bps = float(input("Enter the bandwidth in bits per second (bps): "))

# Convert file size from gigabytes to bits
# 1 byte = 8 bits, 1 GB = 1024^3 bytes = 1,073,741,824 bytes
file_size_bits = file_size_gb * 1073741824 * 8

# Calculate total time in seconds
time_seconds = file_size_bits / bandwidth_bps

# Ask user for preferred time unit
choice = input("Do you want the time in hours, minutes, or seconds? ").lower()


if choice == "seconds":
    print(f"Download time: {time_seconds:.2f} seconds")
elif choice == "minutes":
    time_minutes = time_seconds / 60
    print(f"Download time: {time_minutes:.2f} minutes")
elif choice == "hours":
    time_hours = time_seconds / 3600
    print(f"Download time: {time_hours:.2f} hours")
else:
    print("Invalid choice. Please enter 'hours', 'minutes', or 'seconds'.")


# Task 5
# The user types in an hour (from 0 to 23). If the received value is in the range
# from 0 to 6, print "Good Night"; if from 6 to 13, print "Good Morning"; if from 13 to 17,
# print "Good Day"; if from 17 to 0, print "Good Evening". The upper limit of the range is not
# included. For instance, if 6 is typed in, 6 belongs to the range from 6 to 13.


hour = int(input("Enter the hour (0-23): "))


if 0 <= hour < 24:
    if 0 <= hour < 6:
        print("Good Night")
    elif 6 <= hour < 13:
        print("Good Morning")
    elif 13 <= hour < 17:
        print("Good Day")
    else:  # 17 <= hour < 24
        print("Good Evening")
else:
    print("Invalid hour. Please enter a value from 0 to 23.")
