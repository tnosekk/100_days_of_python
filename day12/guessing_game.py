from random import randint


def play():
    print(
        "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100"
    )
    random_number = randint(0, 100)
    chosen_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if chosen_mode == "easy":
        game(random_number, mode_attempts=10)
    else:
        game(random_number, mode_attempts=5)


def game(random_number, mode_attempts):
    print(f"You have {mode_attempts} attempts remaining to guess the number.")
    attempts = mode_attempts
    user_choice = int(input("Make a guess: "))
    for _ in range(mode_attempts):
        attempts -= 1
        if user_choice == random_number and attempts != 0:
            print(f"Bingo, the number is {random_number}")
            break
        elif user_choice < random_number and attempts != 0:
            print(
                f"Too low!\nYou have {attempts} attempts remaining to guess the number"
            )
            user_choice = int(input("Guess again: "))
        elif user_choice > random_number and attempts != 0:
            print(
                f"Too high!\n You have {attempts} attempts remaining to guess the number"
            )
            user_choice = int(input("Guess again: "))
        elif attempts == 0:
            print("You lost")
            break


if __name__ == "__main__":
    play()
