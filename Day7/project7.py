import random

HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# Your word bank list
word_bank = ["python", "developer", "hangman", "algorithm", "variable", "function"]

# Select a random word
secret_word = random.choice(word_bank)

game_over = False
lives = len(HANGMANPICS) - 1
actual_unique_letters = list(set(secret_word))
predicted_letters = []
wrong_letters = []

print(f"The mystery word is {len(secret_word)} letters long and you have {lives} lives left")

def display_word(actual_word, predicted_letter_list):
    current_letters = ['_' for i in range(len(actual_word))]
    for l in predicted_letter_list:
        for i, al in enumerate(actual_word):
            if l == al:
                current_letters[i] = l
    print(''.join(current_letters), "lives:", lives)


while not game_over:
    letter = input("Guess a letter: ").lower()

    if letter:
        letter = letter[0]
    else:
        continue

    if letter in predicted_letters or letter in wrong_letters:
        print("You already guessed that letter:", letter, "lives:", lives)
        continue
    elif letter in actual_unique_letters:
        predicted_letters.append(letter)
    else:
        lives -= 1
        wrong_letters.append(letter)

    print(HANGMANPICS[len(HANGMANPICS)-lives-1])
    display_word(secret_word, predicted_letters)
    print("=" * 50)

    if len(predicted_letters) == len(actual_unique_letters):
        game_over = True
        print(f"You win! The word was {secret_word}")

    elif lives == 0:
        game_over = True
        print(f"You lose! The word was {secret_word}")
