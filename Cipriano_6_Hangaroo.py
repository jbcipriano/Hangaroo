def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True
def getGuessedWord(secretWord, lettersGuessed):
    result = []
    for i in secretWord:
        if i in lettersGuessed:
            result.append(i)
        else:
            result.append('_')
    return''.join(result)
import string
alph = string.ascii_lowercase
def getAvailableletters(lettersGuessed):
    remain=[]
    for i in alph:
        if i not in lettersGuessed:
            remain.append(i)
    return ''.join(remain)
def hangaroo(secretWord):
    print('Hangaroo')
    print('Guess the word that is', len(secretWord),"letters long.")
    mistakesmade = 0
    lettersGuessed = []
    while 8 - mistakesmade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('============')
            print('Congratulations, HANGAROOOOOOO')
            break
        else:
            print('============')
            print('You have', 8 - mistakesmade, 'guesses remaining.')
            print('letters left:', getAvailableletters(lettersGuessed))
            guess= str(input('Guess a letter:')).lower()
            if guess in secretWord and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print('GOOD JOB!:', getGuessedWord(secretWord, lettersGuessed))
            elif guess in lettersGuessed:
                print("You already pick this one: ", getGuessedWord(secretWord, lettersGuessed))
            elif guess not in secretWord:
                print("Hmmmm not that one: ", getGuessedWord(secretWord, lettersGuessed))
                lettersGuessed.append(guess)
                mistakesmade += 1
            if 8-mistakesmade == 0:
                print('============')
                print('THE WORD IS', secretWord)
                break
            else:
                continue
    
                