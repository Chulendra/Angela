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


def display_word(actual_word, predicted_letter_list):
    # This list comprehension replaces your nested loops
    current_letters = [letter if letter in predicted_letter_list else '_' for letter in actual_word]
    return ' '.join(current_letters)


def play_game():
    word_bank = ["python", "developer", "hangman", "algorithm", "variable", "function"]
    secret_word = random.choice(word_bank)

    max_errors = len(HANGMANPICS) - 1
    errors = 0

    predicted_letters = []
    wrong_letters = []

    print(f"The mystery word is {len(secret_word)} letters long.")
    print(f"You can make {max_errors} mistakes.")

    while True:
        print(HANGMANPICS[errors])
        print("Word:", display_word(secret_word, predicted_letters))
        print(f"Wrong guesses: {', '.join(wrong_letters) if wrong_letters else 'None'}\n")

        # Win Condition
        if set(secret_word).issubset(set(predicted_letters)):
            print(f"🎉 You win! The word was '{secret_word}'.")
            break

        # Loss Condition
        if errors == max_errors:
            print(f"💀 You lose! The word was '{secret_word}'.")
            break

        # Get and validate input
        letter = input("Guess a letter: ").lower()

        # Check if input is empty, too long, or not a letter
        if not letter or not letter[0].isalpha():
            print("⚠️ Please enter a valid letter.")
            print("=" * 50)
            continue

        letter = letter[0]  # Ensure it's only one character

        if letter in predicted_letters or letter in wrong_letters:
            print(f"⚠️ You already guessed '{letter}'. Try again.")
        elif letter in secret_word:
            print(f"✅ Good guess! '{letter}' is in the word.")
            predicted_letters.append(letter)
        else:
            print(f"❌ Sorry, '{letter}' is not in the word.")
            wrong_letters.append(letter)
            errors += 1

        print("=" * 50)


# Run the game
if __name__ == "__main__":
    play_game()