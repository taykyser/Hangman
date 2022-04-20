
import random

HANGMAN_PICS = ['''
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
       ==='''
       ]

words = 'basketball football hockey tennis soccer'.split(' ')

def startGame():
    # This is the welcome function and asks the user if they want to play.
    return input('Welcome to Hangman! Do you want to play? (yes or no)\n').lower().startswith('y')

def getRandomWord(words):
    index = random.randint(0, len(words) - 1)
    return words[index]

def displayBoard(incorrectLetters, correctLetters, chosenWord):
    print(HANGMAN_PICS[len(incorrectLetters)])
    print()
    
    print('Incorrect letters:', end=' ')
    for letter in incorrectLetters:
        print(letter, end=' ')
    print()
    
    blanks = '_' * len(chosenWord)
 
    for i in range(len(chosenWord)): # Replace blanks with correctly guessed letters.
        if chosenWord[i] in correctLetters:
            blanks = blanks[:i] + chosenWord[i] + blanks[i+1:]
    
    for letter in blanks: # Show the chosen word with spaces in between each letter.
        print(letter, end=' ')
    print()
    
def getGuess(alreadyGuessed): # Returns the letter the player entered. This 
# function makes sure the player entered one letter and not something else.
    while True:
        guess = input('Guess a letter: ').lower()
        if len(guess) != 1:
            print('Please enter one letter: ')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again: ')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
      # This function asks the user if they would like to play the game again
      return input('Do you want to play again? (yes or no)').lower().startswith('y')

print('H A N G M A N')
incorrectLetters = ''
correctLetters = ''
chosenWord = getRandomWord(words)
gameIsDone = False

if startGame():
    while True:
            
        displayBoard(incorrectLetters, correctLetters, chosenWord)
        # Let the player enter a letter.
        guess = getGuess(incorrectLetters + correctLetters)
        if guess in chosenWord:
            correctLetters = correctLetters + guess
        # Check if the player has won.
            foundAllLetters = True
            for i in range(len(chosenWord)):
                if chosenWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is', chosenWord ,
                    'WINNER!')
                gameIsDone = True
        else:
            incorrectLetters = incorrectLetters + guess

# Ths checks to see if the player guessed too many times and lost.
        if len(incorrectLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(incorrectLetters, correctLetters, chosenWord)
            print('You have run out of guesses!\nAfter ' +
                str(len(incorrectLetters)) + ' incorrect guesses and ' + 
                str(len(correctLetters)) + ' correct guesses,' +
                'the word was "' + chosenWord + '"')
            gameIsDone = True

    # Whn the game is done this asks the player if they want to play again.
        if gameIsDone:
            if playAgain():
                incorrectLetters = ''
                correctLetters = ''
                gameIsDone = False
                chosenWord = getRandomWord(words)
            else:
                break
