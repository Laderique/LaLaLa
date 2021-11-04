#Need to import some built in functions stored in python 
import random               #Choose randomly from list 
from words import words     #Getting words from word list that were Imported | global varible 
import string               #Import a list of uppercase letters 
import time                 #Call time function to slow down certain steps in the programs 

#Need to get a valid string that computer can pull from 
def valid_word (words):
    word = random.choice(words)                             #Chooses something from list of imported words
    while '-' in word or ' ' in word:                       #Some words have dashes and spaces in the list 
        word = random.choice(words)                         #While word has dash or space keep choosing words until 
                                                                               #...word does not have space or dash  
    return word.upper()                                     #Return word in all upper case | upper case will be put on all letters
                                                                                         #...in program to make comparisons easier 
#Writing game as function so that it can be used for other things                                                         
def hangman():
    print('Welcome to Hangman! I Wish you the best of luck. Good luck and remeber to have fun.') #Introduction to help make the game fun 
    time.sleep(1)                                          #A time thats not too rushed or too slow 
    lives= int(input('How many lives would you like? '))   #Getting amount of lives user wants storing as a variable to use later 
    word = valid_word(words)                               #Calling valid function and storing valid word as a local varible
    words_letters= set(word)                                #Save letters in valid word as a set to compare 
    alphabet = set(string.ascii_uppercase)                 #Taking the alphabet provided by built in function making it all upper case and storing as a variable
    letters_used = set()                                   #Empty set to keep track of and store what the user has guessed
     
     
    while len(words_letters) > 0 and lives > 0:            #need to loop as until word is guessed fully
                                                           #while conditions: while the length of word letters is greater than 0 
                                                                                  #...and lives are greater than zero keep going
         
        #Need to tell the user what the current word is with dashes in the place of missing letters 
        #List comprehension combined with Ternary conditional 
        #Python implementation of Set builder notation synatic sugar
        #Here letter is a variable that is used for iterating over a sequence(word) 
        #On every iteration it takes the next value from word until the end of sequence is reached
        word_list = [letter if letter in letters_used else '_' for letter in word] 
        
        time.sleep(.7)
        print('Current word: ',' '.join(word_list))         #Join() function in python takes all items in an iterable (function/object
        time.sleep(.5)                                      #Delay    #...that can be repeated over and over and joins them in one string
        print('You have', lives,'lives and you have used these letter(s): ',' '.join(letters_used))    #Tell user how many lives left and what letters are used | The .join takes the used letters and seperates by what is put before it
        user_letter= input("Guess a letter: ").upper()      #Getting the letter a user inputs | Turning letter uppercase 
        if user_letter in alphabet - letters_used:          #Taking used letters out of alphabet string and seeing if user's guess is in the alphabet                
            letters_used.add(user_letter)                   #If users guess is in the alphabet still add user's input to the empty string
            if user_letter in words_letters:                #If statement to check if user's letter is in the word's letters 
                words_letters.remove(user_letter)           #Removing the user's guessed letter from the word's set of letters
            else:                                           #Else statement where it is needed to make hang man hangman | put here because user's guess is already being compared to word's letters
                lives -= 1                                  #Taking a life from lives, it's hangman 
                time.sleep(1)                               #Pause so game doesnt feel rushed
                print('Sorry, your letter was not in the word. Try one more time!') #Keeping frustration to a minimum 
                time.sleep(.5)                              #Delay
        elif user_letter in letters_used:                   #If letter has been used already: inform the user 
            time.sleep(1)                                   #Delay
            print("You have already used that character. Please try again.")
            time.sleep(1)                                   #Delay 
        else:                                               #Inform user if what they have typed can not be used 
            print("Invalid character. Please try again.")
            time.sleep(1)                                   #Delay
    #One of the while loops parameters for ending has been met | user either lost or won  
    if lives == 0:                                          #If lives are out tell user that they have lost
        time.sleep(1)                                       #Dlay 
        print('Sorry, you have no lives. Sucks to suck.')
    else:                                                   #If the user still has lives and a while loop's parameter has been met the user has Won | Tell them    
        time.sleep(1)                                       #Delay
        print('The word was',word,'.Great job!')
    
hangman()                                                   #Calling The hangman function 


#REFERENCES
#https://www.randomlists.com/data/words.json                                                    Reference for python examples of functions
#https://docs.python.org/3.9/reference/expressions.html                                         Python Language reference/expressions/syntax
#https://stackoverflow.com/questions/6475314/python-for-in-loop-preceded-by-a-variable          List Comprhension 
#https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions                     List Comprehension
#https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator     Ternary conditional operator
#https://docs.python.org/2/reference/expressions.html#conditional-expressions                   Conditional Expressions
#https://beginnersbook.com/2018/01/python-for-loop/                                             To help uderstand for loops and why I can combine for loop and if else statement 
#https://www.randomlists.com/data/words.json                                                    List of 5000 words to import and use 
#https://www.geeksforgeeks.org/python-projects-beginner-to-advanced/                            Project Ideas 
#https://www.geeksforgeeks.org/hangman-game-python/                                             Project summary and overview of how it should look 