import random
playing = True
number = str(random.randint(1, 10))

print("Welcome to the Number Guessing Game!")

print("I have selected a number between 1 and 10. Can you guess it?")

while playing:

    guess = input("Enter your guess: ")

    if guess == number:
        print("Congratulations! You guessed the number!")
        playing = False

        break

    else:
        print("Wrong guess. Try again!")