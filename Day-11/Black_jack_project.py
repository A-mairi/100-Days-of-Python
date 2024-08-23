import random
import Blackjack_art


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Compares the user score against the computer score."""
    if u_score == c_score:
        return 'It is a Draw!'
    elif u_score == 0:
        return 'You Win with a Blackjack!'
    elif c_score == 0:
        return 'You Lose, opponent has a Blackjack.'
    elif u_score > 21:
        return 'You Lose, you went over 21.'
    elif c_score > 21:
        return 'You Win! opponent went over 21.'
    elif u_score > c_score:
        return 'You Win! your score is higher than your opponent.'
    else:
        return 'You Lose, your opponent\'s score is higher than yours.'


def black_jack():
    print(Blackjack_art.logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Your cards are: {user_cards}, your current score is: {user_score}.')
        print(f'Computer\'s first card is: {computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            ask_user = input('Type \'y\' to get another card, or type \'n\' to pass. ').lower()
            if ask_user == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f'Your final hand is {user_cards} and your final score is: {user_score}.')
    print(f'Computer\'s final hand is {computer_cards} and computer\'s final score is {computer_score}.')
    print(compare(user_score, computer_score))


while input('Would you like to play a game of Blackjack? Type \'yes\' or \'no\'. ').lower() == 'yes':
    print('\n' * 20)
    black_jack()
