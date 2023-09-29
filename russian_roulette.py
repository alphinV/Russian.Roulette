import random

def russian_roulette_game():
    while True:
        print("Welcome to the Number Russian Roulette Game!")
        print("I have chosen a random number between 1 and 10.")
        print("You have 3 attempts to guess the correct number.")

        secret_number = random.randint(1, 10)
        attempts = 3

        while attempts > 0:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 10.")
                continue

            if guess == secret_number:
                print("Congratulations! You guessed the correct number:", secret_number)
                break
            elif guess < secret_number:
                print("Try again. Your guess is too low.")
            else:
                print("Try again. Your guess is too high.")

            attempts -= 1

        if attempts == 0:
            print("You've run out of attempts. The secret number was:", secret_number)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    russian_roulette_game()
