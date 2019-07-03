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

    def __init__(self):
        pass

#selecting from a category loop
    def selectCategory(self):
        while True:
            print(' ')
            print('Welcome to Hang-man.')
            print(' ')
            print('Select a category to play from.')

        #selecting category input
            question = input('Famous People or Movies')
            if question.lower() == 'famous people':
                print('inside famous people')
                self.selectWord()
                break
            elif question.lower() == 'movies':
                print('inside movies')
                self.selectWordTwo()
                break



#selects word for the category 'famous people' based on the number sent
    def selectWord(self):
        wordbank = ['Miley Cyrus', 'Tom Delonge', 'Bill Murray', 'Morgan Freeman','Keith Richards']
        print(wordbank[random.randint(0,4)])



#selects word for the category 'tv shows' based on the number sent
    def selectWordTwo(self):
        wordbank = ['Interstellar', 'Planet of the Apes', 'The Departed', 'Wolf of Wall Street','Source Code']
        print(wordbank[random.randint(0,4)])


g = game()
g.selectCategory()
