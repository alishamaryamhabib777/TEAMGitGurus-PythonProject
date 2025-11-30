#DEFINING FUNCTION
import random
def guess_number():
    while True:
        target = random.randint(1, 50)
        attempts = 0
        print("Guess the number (1 to 50). Type '0' to quit.")
        while True:
            guess = input("Your guess:").strip()
            if guess.lower() == '0':
                print("Exiting game")
                return
            try:
                g = int(guess)
            except ValueError:
                print("Please enter a number between 1 and 50 or '0' to quit")
                continue
            attempts += 1
            if g < target:
                print("Your guess is too low")
            elif g > target:
                print("Your guess is too high")
            else:
                print(f"Correct! You guessed in {attempts} attempt(s).")
                break
        again = input("Want to play again? (y/n):").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break
#CALLING FUNCTION
guess_number()