import random
from Number_Guessing_Art import logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


# Function to check user's guess against the correct answer
def check_number(user_guess, correct_answer, attempts):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > correct_answer:
        print('Too High.')
        return attempts - 1
    elif user_guess < correct_answer:
        print('Too Low.')
        return attempts - 1
    else:
        return 0  # Return 0 to indicate the correct answer was guessed


# Function to choose the game difficulty
def choose_difficulty():
    difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ').lower()
    if difficulty == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS


def game():
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print('I\'m thinking of a number between 1 and 100.')

    correct_number = random.randint(1, 100)
    turns = choose_difficulty()

    while turns > 0:
        print(f'You have {turns} attempts remaining to guess the correct answer.')
        user_guess = int(input('Guess a number: '))
        turns = check_number(user_guess, correct_number, turns)

        if turns == 0:
            if user_guess == correct_number:
                print(f'Congratulations! You guessed the correct number: {correct_number}!')
            else:
                print(f'You Lost. The correct number was {correct_number}.')
            return  # Exit the game after guessing correctly or running out of attempts


game()
