# Hangman Project

#Steps:
#         *Clear output everytime?
#Welcome: Welcome to hang-man - and display categories - 2 categories of 5 words each chosen at random.
#When selected print the number of tiles in the word and 'Please enter a letter'
#if letter is in the word, replace the tile with the word(for each letter if multiple) if not - minus from lives



#from IPython.display import clear_output
#i can't use ipython currently so i commented it for now
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
            question = input('Famous People or Movies: ')
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
        selected=wordbank[random.randint(0,4)]
        self.backgroundwork(selected)
        

#selects word for the category 'tv shows' based on the number sent
    def selectWordTwo(self):
        wordbank = ['Interstellar', 'Planet of the Apes', 'The Departed', 'Wolf of Wall Street','Source Code']
        selected=wordbank[random.randint(0,4)]
        self.backgroundwork(selected)

#Modifications by user Erokhar
    def backgroundwork(self,selected):
        inputted=""
        currentLine=[]
        currentLineString=""
        s=""
        lives=5
#setting the list for use
        for x in selected:
            if(x!=" "):
                currentLine.append("_")
            else:
                currentLine.append(" ")
        for x in currentLine:
            s+=x
        print(s)

        while currentLineString.lower()!=selected.lower():
            found=0
            currentLineString=""
            inputted=input("input letter: ")
#iterating around the given string and checking for the input letter inside
            for x in range(len(selected)):
                if selected[x].lower()==inputted.lower():
                    currentLine[x]=inputted
                    found=1
            if found!=1:
                if lives>1:
                    lives-=1

                    print("Wrong! lives left: ", lives)
                else:
                    print("No more lives. GAME OVER!")
                    print("The answer was: ", selected)
                    return 0
#Making a space....well space in the list
            if selected[x]==" ":
                currentLine[x]=" "
#setting the final string that will be compared with the original selected word
            for x in currentLine:
                currentLineString+=x
            print(currentLineString)
                
        print("Congratulations! The answer was: ", currentLineString)




g = game()
g.selectCategory()

