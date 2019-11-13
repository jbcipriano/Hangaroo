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
                print('The word is', secretWord)
                break
            else:
                continue
    
                