import random

secret_number = random.randint(1, 100)

max_attempts = 5
attempts = 0

print("Welcome to the Number Guessing Game!")
print(f"Try to guess the secret number between 1 and 100. You have {max_attempts} attempts.")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Try higher.")
        else:
            print("Try lower.")
    except ValueError:
        print("Please enter a valid number.")

if attempts == max_attempts:
    print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}.")
