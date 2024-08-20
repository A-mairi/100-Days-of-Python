from Blind_Auction_Art import logo

print(logo)
print('Welcome to Blind Auction')


def find_highest_bidder(bidding_dictionary):
    winner = ''
    highest_bid = 0

    for bidder in bidding_dictionary:
        bidding_amount = bidding_dictionary[bidder]
        if bidding_amount > highest_bid:
            highest_bid = bidding_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of €{highest_bid}.')


blind_auction = {}
Bidding = True
while Bidding:

    name = input('What is your name?: ')
    bid_amount = int(input('How much would you like to bid?: €'))

    blind_auction[name] = bid_amount

    Extra_bidders = input('Are there any other bidders? Type \'yes\' or \'no\'. \n').lower()
    if Extra_bidders == 'yes':
        print('\n' * 35)

    elif Extra_bidders == 'no':
        Bidding = False
        print('\n' * 35)
        find_highest_bidder(blind_auction)
