# Hangman Project

#next time condense the main game function, otherwise it is too much to change after you get everything working 'properly'
#everything else if pretty much condensed, main function is only problem
#and its very hard to read my code

#but I know this for next time*

#instead of setting different if's if input is incorrect, set a list to the abc's, and if the user enters a special
#character or a random word, throw an exception. Makes it way easier than what


#imports
from IPython.display import clear_output
import random
import sys

class game():

    def __init__(self):
        self.words = []
        self.life = 10
        self.wlist = []
        self.wlist2 = []


#selecting from a category loop
    def selectCategory(self):
        print(' ')
        print('Welcome to Hang-man.')
        print(' ')
        print('Select a category to play from.')

        #selecting category input
        while True:
            try:
                question = input('Famous People or Movies')
                if question.lower() == 'famous people':
                    self.selectWord()
                    break
                elif question.lower() == 'movies':
                    self.selectWordTwo()
                    break
                else:
                    clear_output()
                    print("Please enter a valid category.")
            except:
                clear_output()
                print('You have exited the game.')
                break

#selects word for the category 'famous people' based on the number sent
    def selectWord(self):
        clear_output()
        wordbank = ['Miley Cyrus', 'Tom Delonge', 'Bill Murray', 'Morgan Freeman','Keith Richards']
        self.linesForWord(wordbank[random.randint(0,4)])

#selects word for the category 'tv shows' based on the number sent
    def selectWordTwo(self):
        clear_output()
        wordbank = ['Interstellar', 'Planet of the Apes', 'The Departed', 'Wolf of Wall Street','Source Code']
        self.linesForWord(wordbank[random.randint(0,4)])

#accepts word, and finds which number of lines to print
    def linesForWord(self, word):
        clear_output()
        self.word = word     #dont think i need this
        #where lists were
        for w in range(len(self.word)):
#             print(self.word[w], end = ' ')
            if self.word[w] != " ":
                self.wlist.append("_")
            else:
                self.wlist.append(" ")
            self.wlist2.append(self.word[w].lower())
        self.gamePlay(self.wlist, self.wlist2)


#where the gameplay is played and input is asked
#next time condense so function is not doing multiple tasks
#i can put each task in a function and just call the function, the gameplay function just calls a bunch of functions

    def gamePlay(self, wlist, wlist2):

        while True:
            for i in range(len(wlist)):
                print(wlist[i], end=" ")
            n = input('Choose a letter: ')
            clear_output()
            n = n.lower()
            if n == 'quit':                #base case to quit.
                break
            if len(n) >= 2:
                print("Please enter only 1 letter per guess.")
                self.lettersChosen(None)
                continue
            try:
                if int(n):
                    print("Please enter letters only.")
            except:
                pass
            if n in wlist2:
                for i in range(len(wlist2)):
                    if n == wlist2[i]:
                        del(wlist[i])
                        wlist.insert(i, n)
                self.lettersChosen(None)
            else:
                self.lettersChosen(n)
            if wlist == wlist2:
                self.wonGame()

#displays which letters are chosen
    def lettersChosen(self, word):     # 'word' even tho its a letter haha.
        s = self.checkLetter(word)
        if s == True:
            print(  "\tLetters Chosen"  )
            print("–––––––––––––––––––––––––––––––––")
            print(" ")
            for i in range(len(self.words)):
                print(self.words[i], end = ' ')
            print(" ")
            print(" ")
            return           #this whole section i don't know how to condense this...
        if word == None:
            print("                                                                        Number of lives: " + str(self.life))
            pass
        else:
            self.words.append(word)
            self.lives(self.life)
        print(  "\tLetters Chosen"  )
        print("–––––––––––––––––––––––––––––––––")
        print(" ")
        for i in range(len(self.words)):
            print(self.words[i], end = ' ')
        print(" ")
        print(" ")
        return


#checks if letter guessed is already guessed.
    def checkLetter(self, word):
        if word in self.words:
            print("                                                                        Number of lives: " + str(self.life))
            print(f'The letter \'{word}\' is already guessed.')
            print(" ")
            return True
        else:
            return


#returns numbers of lives left
    def lives(self, life):
        self.life = life-1
        if self.life <= 0:
            self.lostGame()
        print("                                                                        Number of lives: " + str(self.life))
        return

#when game is lost, this is called
    def lostGame(self):
        clear_output()
        print("Sorry, you ran out of lives.")
        print(' ')
        n = input('Would you like to play again? (y or n) ')
        self.endGame(n)

#checks whether the user wants to play again
    def endGame(self, n):
            clear_output()
            if n.lower() == 'y':
                self.wlist = []              #new instance enables the game to restart without clearing all lists
                self.wlist2 = []
                self.words = []
                self.life = 10
                g.selectCategory()
                sys.exit()
            if n.lower() == 'n':
                clear_output()
                print(' ')
                print("Thanks for playing")
                sys.exit()                   #tosses an exception but is caught by outer try / catch

#the win game exit screen
    def wonGame(self):
        clear_output()
        print('Congrats, you have won the game!')
        print(' ')
        n = input('Would you like to play again? (y or n) ')
        self.endGame(n)


g = game()
g.selectCategory()
