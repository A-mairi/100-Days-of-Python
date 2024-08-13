# Coin Flip
import random
coin_flip = random.randint(1, 2)

print('Welcome to the coin flipper.')
start = input('Type \'Flip\' to flip a coin.\n').lower()

if coin_flip == 1:
    print('It is Heads!')
else:
    print('It is Tails!')
