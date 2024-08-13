# Love Calculator Project
print("Welcome to the Love Calculator")
print('The calculator checks for the number of times the letters in the word TRUE and LOVE occur in both names')


name1 = input('Please enter your name: ')
name2 = input('Please enter your partner\'s name: ')

combined_names = name1 + name2
lower_case = combined_names.lower()

T = lower_case.count('t')
R = lower_case.count('r')
U = lower_case.count('u')
E = lower_case.count('e')
total_true = T + R + U + E

L_1 = lower_case.count('l')
O_1 = lower_case.count('o')
V_1 = lower_case.count('v')
E_1 = lower_case.count('e')
total_love1 = L_1 + O_1 + V_1 + E_1

score = int(str(total_true) + str(total_love1))

print('The Love Calculator is calculating your score ...')

if score < 10 or score > 90:
    print(f'Your score is: {score}, you go together like coke and mentos.')
elif 40 <= score <= 50:
    print(f'Your score is: {score}, you are alright together.')
else:
    print(f'Your score is: {score}.')
