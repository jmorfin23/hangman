# Hangman Project

#Steps:
#         *Clear output everytime?
#Welcome: Welcome to hang-man - and display categories - 2 categories of 5 words each chosen at random.
#When selected print the number of tiles in the word and 'Please enter a letter'
#if letter is in the word, replace the tile with the word(for each letter if multiple) if not - minus from lives



#imports
from IPython.display import clear_output
import random

class game():
    words = []
    def __init__(self):
        pass

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
                print("Please select a valid category.")
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
        wlist = []           #i can make a global list l8r
        wlist2 = []
        for w in range(len(self.word)):
            print(self.word[w], end = ' ')
            if self.word[w] != " ":
                wlist.append("_")
            else:
                wlist.append(" ")
            wlist2.append(self.word[w])
        self.gamePlay(wlist, wlist2)

#where the gameplay is played and input is asked
    def gamePlay(self, wlist, wlist2):
        print('inside gameplay')
        print(wlist)
        print(wlist2)
        while True:
#             clear_output()
            n = input('Choose a letter: ')
            if n in wlist2:
                for i in range(len(wlist2)):
                    if n == wlist2[i]:
                        wlist.insert(i, n)
                        print(wlist[i], end=" ")
                    else:
                        print(wlist[i], end=" ")
            else:
                self.lettersChosen(n)     #this isnt called
                print('this letter is not in word')



#displays which letters are chosen
    def lettersChosen(word):
        words.append(word)
        print(  "\tLetters Chosen"  )
        print("–––––––––––––––––––––––––––––––––")
        print(" ")
        for i in range(len(words)):
            print(words[i], end = ' ')

            

g = game()
g.selectCategory()
