# Task 2
# Develop a game of Bulls and Cows. The program chooses a four-digit number,
#  and the player has to guess it. After the user enters a number, the program
# reports how many digits of the number are guessed (bulls), and how many digits
# are guessed and stand in the right place (cows). After guessing the number,
# print the number of user's attempts. Use recursion in your game.

import random


def generate_number():
    return str(random.randint(1000, 9999))


def count_bulls_and_cows(secret, guess):
    cows = sum(s == g for s, g in zip(secret, guess))
    bulls = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - cows
    return bulls, cows


def play(secret, attempts=1):
    guess = input(f"Attempt {attempts}: Enter your 4-digit guess: ")

    if not guess.isdigit() or len(guess) != 4:
        print("❌ Invalid input! Please enter exactly 4 digits.")
        return play(secret, attempts)

    bulls, cows = count_bulls_and_cows(secret, guess)
    print(f"➡️ Bulls: {bulls}, Cows: {cows}")

    if guess == secret:
        print(
            f"🎉 Congratulations! You guessed the number {secret} in {attempts} attempts."
        )
    else:
        return play(secret, attempts + 1)


# Start the game
if __name__ == "__main__":
    secret_number = generate_number()
    print("🐮 Welcome to Bulls and Cows! Guess the 4-digit number.")
    play(secret_number)
