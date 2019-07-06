# Hangman Project

#Steps:
#         *Clear output everytime?
#Welcome: Welcome to hang-man - and display categories - 2 categories of 5 words each chosen at random.
#When selected print the number of tiles in the word and 'Please enter a letter'
#if letter is in the word, replace the tile with the word(for each letter if multiple) if not - minus from lives



#imports
from IPython.display import clear_output
import random
import sys

class game():

    def __init__(self):
        self.words = []
        self.life = 10


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
            except:
                print(' ')
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
        wlist = []
        wlist2 = []
        for w in range(len(self.word)):
#             print(self.word[w], end = ' ')
            if self.word[w] != " ":
                wlist.append("_")
            else:
                wlist.append(" ")
            wlist2.append(self.word[w].lower())
        self.gamePlay(wlist, wlist2)


#where the gameplay is played and input is asked
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

#when game is lost, this is called to exit or restart the program
    def lostGame(self):
        clear_output()
        print("Sorry, you ran out of lives.")
        print(' ')
        n = input('Would you like to play again? (y or n) ')
        clear_output()
        if n.lower() == 'y':
            g.selectCategory()
            sys.exit()
        if n.lower() == 'n':
            clear_output()
            print(' ')
            print("Thanks for playing")
            sys.exit()                   #tosses an exception but is caught by outer try / catch

g = game()
g.selectCategory()
