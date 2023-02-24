import random
import hangman_words        #alternative: from hangman_words import word_list

hangman = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
        |
       ===''', '''
   +---+
   O   |
   /|\  |
        |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

random_word = random.choice(hangman_words.word_list)
len_random_word = len(random_word)
life = 0
blanks = []
for letter in random_word:
    blanks += "_"

print(f"Welcome to Hangman!\n {hangman[life]}")
print(f"Your word has {len_random_word} letters. {' '.join(blanks)}")


while life != 6:
    if not "_" in blanks:
        print("Gamer Over! You WIN!")
    guess = input("Guess a letter: ")
    if not guess in random_word:
        life += 1
        print(' '.join(blanks))
        print("There is no such letter in the word.")
        print(hangman[life])
    elif guess in random_word:
        for position in range(len_random_word):
            letter = random_word[position]
            if blanks[position] == guess:
                print("You've already guessed that letter.")
            elif letter == guess:
                blanks[position] = guess
        print(' '.join(blanks))
        print(hangman[life])
print(f"Game Over! You Lose. The word is {random_word}.")
    