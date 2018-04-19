from random import *

##
# Author: Alex Metz (alex.tar.gz@gmail.com)
##

# Logic Section
def buildWordList(fileName):
    with open('assets\{}'.format(fileName), 'r') as wordFile:
        words = wordFile.read()
        wordList = []
        for word in words.split():
            wordList.append(word)

    startGame(wordList)

def searchList(characterList, userSelection, guessList, correctList):
    startPos = -1
    if(userSelection in guessList):
        print("You guessed that letter already. (Note: This counts against your guesses.)")
    else:
        while True:
            try:
                location = characterList.index(userSelection, (startPos + 1))
            except ValueError:
                break
            else:
                correctList.insert(location, userSelection)
                print(userSelection)
                guessList.append(userSelection)
                startPos = location
    return correctList

def startGame(wordList):
    i = randint(0, len(wordList))
    randomWord = wordList[i]
    characterList = []
    for char in randomWord:
        characterList.append(char)

    print("Welcome to PyHangman! There are {} letters in your random word. Good luck!".format(len(characterList)))
    print("If you know the word, enter it as a guess. If you're done, enter 0 and the program will exit.")

    guessAmount = 0
    guessList = []
    correctList = []
    while(guessAmount < 8):
        userSelection = raw_input("\nEnter your guess ({}): ".format(9 - (guessAmount + 1)))
        guessAmount = (guessAmount + 1)
        if(userSelection == randomWord) or (correctList == characterList):
            print("\n" + "You won!")
            exit()
        elif(userSelection == "0"):
            print("Thanks for playing!")
            exit()
        elif(characterList[0:len(characterList)]):
            correctList = searchList(characterList, userSelection, guessList, correctList)
    print("\n" + "The correct word was: {}".format(randomWord) + "\n" + "Your guesses were: {}".format("".join(correctList)))

buildWordList("words.txt")
