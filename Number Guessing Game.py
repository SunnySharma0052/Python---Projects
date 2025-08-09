# 🔹Project – Number Guessing Game
# 🎮 Goal:-
# Computer picks a number
# You guess until correct
# Shows how many attempts you used

import random
secret = random.randint(1, 10)
guess = None
attempts = 1
print("Guess a number between 1 and 10")

while guess != secret:
    guess =int(input("Enter your Guess number:"))
    attempts += 1
    if guess < secret:
        print("Too Low!")
    elif guess > secret:
        print("Too High!")
    else:
        print("Correct! Attmpts:", attempts)
