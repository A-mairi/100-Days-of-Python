import random
# Display art
import Higher_Or_Lower_Art
import game_data

def formated_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account['name']
    account_description = account['description']
    account_origin = account['country']
    return f'{account_name}, a {account_description}, from {account_origin}.'

def compare_date(user_guess, followers_a, followers_b):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if followers_a > followers_b:
        return guess == 'a'
    else:
        return guess == 'b'


print(Higher_Or_Lower_Art.logo)
score = 0
continue_game = True
# Generate a random account from the game data
account_b = random.choice(game_data.data)

# Make the game repeatable
while continue_game:

    # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(game_data.data)

    if account_a == account_b:
        account_b = random.choice(game_data.data)

    print(f'Compare A: {formated_data(account_a)}.')
    print(Higher_Or_Lower_Art.vs)
    print(f'Compare B: {formated_data(account_b)}.')

    # Ask user for a guess.
    guess = input('Who do you think has more followers? Type \'A\' or \'B\': ').lower()

    # Clear the screen
    print('\n' * 25)
    print(Higher_Or_Lower_Art.logo)

    # - Get follower count of each account
    follower_count_a = account_a['follower_count']
    follower_count_b = account_b['follower_count']

    # Check if the user is correct
    is_true = compare_date(guess, follower_count_a, follower_count_b)

    # Give the user feedback.
    # Score keep
    if is_true:
        score += 1
        print(f'That is correct! current score is: {score}')
    else:
        print(f'Sorry, your answer was incorrect. Game Over. Final Score: {score}')
        continue_game = False
