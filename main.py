def main():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Smart Calculator")
        print("2. Guess the Number Game")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            Smart_Calculator()
        elif choice == '2':
            guess_number()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
#-----------------------------SMART CALCULATOR-------------------------------------
#DEFINING FUNCTION
def Smart_Calculator():
    print("Welcome to the Smart Calculator")
    while True:
        print("\n--- Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '5':
            print("Exiting...")
            break
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                print("Result:", num1 + num2)
            elif choice == '2':
                print("Result:", num1 - num2)
            elif choice == '3':
                print("Result:", num1 * num2)
            elif choice == '4':
                if num2 == 0:
                    print("Error: You cannot divide by zero!")
                else:
                    print("Result:", num1 / num2)
        else:
            print("Invalid choice, please try again.")

#---------------------------GUESSING NUMBER GAME---------------------------------

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
main()

#-----------------------------USER FRIENDLY OUTPUT--------------------------

#----------------------------------END-----------------------------------