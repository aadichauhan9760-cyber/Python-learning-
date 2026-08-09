import random


def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("=" * 40)
    print("       NUMBER GUESSING GAME")
    print("=" * 40)
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > 100:
                print("⚠️ Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("📉 Too low! Try again.")

            elif guess > secret_number:
                print("📈 Too high! Try again.")

            else:
                print("\n🎉 Congratulations!")
                print(f"You guessed the correct number: {secret_number}")
                print(f"Number of attempts: {attempts}")
                break

        except ValueError:
            print("❌ Please enter a valid number.")


if __name__ == "__main__":
    number_guessing_game()
