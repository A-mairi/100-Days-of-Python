import random
import hangman_words
import hangman_art


word_list = hangman_words.word_list
lives = 6
stages = hangman_art.stages


print('Welcome to the game:')
logo = hangman_art.logo
print(logo)
chosen_word = random.choice(word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    
    print(f"You have: {lives}/6 LIVES")
    guess = input("Guess a letter: ").lower()

    
    if guess in correct_letters:
        print(f'You have already guess: {guess}. Please choose another letter.')

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)


    if guess not in chosen_word:
        lives -= 1
        print(f'You guessed {guess}, that letter is not in the word.')
        if lives == 0:
            game_over = True
            print(f"You ran out of lives. The word was {chosen_word}!\nYOU LOSE.")

    if "_" not in display:
        game_over = True
        print("Congratulations, you have guess the word. YOU WIN!")

    
    print(stages[lives])
