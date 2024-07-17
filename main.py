import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

gameOver = False
chosenWord = random.choice(word_list)
word_length = len(chosenWord)
lives = 6
print(logo)


display = []
for _ in range(word_length):
    display += "_"

while not gameOver:

    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosenWord[position]
        
        if letter == guess:
            display[position] = letter
    
    if guess not in chosenWord:
        lives -= 1
        if lives == 0:
            gameOver = True
            print("You lose.")
        
    print(f"{" ".join(display)}")

    
    if "_" not in display:
        gameOver = True
        print("You win.")

    print(stages[lives])
    
        


