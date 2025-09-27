import random

def guess_game():
    print("🎯 Welcome to the Perfect Guess Game! 🎯")
    print("I have selected a number between 1 and 100.")
    print("Can you guess it?")

    # Random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! 📉 Try again.")
            elif user_guess > number_to_guess:
                print("Too high! 📈 Try again.")
            else:
                guessed = True
                print(f"🎉 Congratulations! You guessed the number {number_to_guess} in {attempts} attempts!")
        except ValueError:
            print("❌ Please enter a valid integer.")

if __name__ == "__main__":
    guess_game()

 
