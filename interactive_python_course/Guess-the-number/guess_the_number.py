# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
# author sturrion

import simplegui
import random
import math

# intialize globals
num_range = 100

# helper function to start and restart the game
def new_game():
    """ initializes global variables and print new game message """
    
    # initializes a global variable secret_number to be a 
    # random number in the range [0, num_range). 
    global secret_number
    secret_number = random.randrange(0, num_range)
    
    # any secret number in the range [low, high) can always 
    # be found in at most n guesses where n is the smallest 
    # integer such that 2 ** n >= high - low + 1
    global remaining_guesses
    remaining_guesses = int(math.ceil(math.log(num_range - 0 + 1, 2)))
    
    # Prints a new line and the new game message
    print "" 
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is", remaining_guesses
    
def bad_guess():
    """ If the guess is not the correct, updates remaining_guesses, 
    prints the message, and starts a new game """
    
    global remaining_guesses
    remaining_guesses -= 1
    
    print "Number of remaining guesses is", remaining_guesses

    if remaining_guesses == 0:
        print "You ran out of guesses. The number was", secret_number
        new_game()
        

# define event handlers for control panel
def range100():
    """ changes the range to [0,100) and starts a new game """
    global num_range
    num_range = 100
    
    new_game()
    
def range1000():
    """ changes the range to [0,1000) and starts a new game """
    global num_range
    num_range = 1000
    
    new_game()
    
def input_guess(guess):
    """ Takes the input string guess, 
        converts it to an integer, 
        prints out a message of the form "Guess was 37",
        compares the entered number to secret_number, 
        prints out an appropriate message,
        and call the function related to each case
    """
    print "" 
    
    number_guess = int(guess)
    print "Guess was", guess
    
    # main game logic goes here	
    if secret_number == number_guess:
        print "Correct!"
        new_game()
    elif secret_number > number_guess:
        print "Higher!"
        bad_guess()
    else:
        print "Lower!"
        bad_guess()
        
    
# create frame
frame = simplegui.create_frame("Guess the number",300,300)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess , 200)

frame.start()

# call new_game 
new_game()


