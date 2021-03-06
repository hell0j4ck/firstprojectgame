from random import shuffle

#This is my second python project. I'm creating a game where you need to guess the ball's location under the cup
#The functions are listed below before the final script

#This is the function that shuffles our list 
def shuffle_list(mylist):
        shuffle(mylist)
        return mylist


#This is the function to take the player's guess
def player_guess():
    
    guess = '' #PLACEHOLDER
    
    #if guess not 0 or 1 or 2, keep prompting the player to guess
    while guess not in ['0','1','2']:
        
    
        guess = input("Pick a number 0, 1, or 2")

        
    return int(guess) #return the guess as an integer to use for indexing to determine if the guess is right via the position of 'O'



#This is the function to check the player's guess 
def check_guess(mylist, guess):
    #if the guess returns 'O' from indexing, the player is correct
    if mylist[guess] == 'O':

        print('CORRECT!')
        
    else:

        print("Wrong Guess!")

        print(mylist)
    #I JUST PUT THAT THERE SO THE TERMINAL WON'T AUTOCLOSE AFTER I GET AN OUTPUT
    return input('Did you enjoy this game?')



#First I will start with my initial list containing the ball 'O' with the empty strings defining an empty cup
mylist = ['','O','']

#NOW SHUFFLING THE LIST
mixedup_list = shuffle_list(mylist)

#USER GUESS HERE
guess = player_guess()

#CHECK THE GUESS
check_guess(mixedup_list, guess)
