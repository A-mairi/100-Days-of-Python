# Rock Paper Scissors
import random

print('Welcome to Rock, Paper, Scissors!')

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

RPS = [rock, paper, scissors]

player = int(input('What would you like to choose?'
                   'Type 0 for Rock, Type 1 for Paper or 2 for Scissors.\n'))

if player >= 3 or player < 0:
    print('You typed an invalid number, you lost.')

else:
    print(RPS[player])
    computer = random.randint(0, 2)
    print('Computer chose:')
    print(RPS[computer])

    if player == 0 and computer == 2:
        print('You Won!')
    elif computer == 0 and player == 2:
        print('You Lost.')
    elif computer > player:
        print('You Lost.')
    elif player > computer:
        print('You Won!')
    elif player == computer:
        print('It\'s a Draw!')
