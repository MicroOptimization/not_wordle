from word_set import *
import random

def show_intro():
    print("This is definitely not Wordle.")
    print("Y: Right place Right letter")
    print("S: Wrong place Right letter")
    print("N: Wrong place Wrong letter")
    print("Now give me a 5 letter word")
    print()
    
def get_valid_guess():
    cur_guess = input("Enter guess #{}: ".format(guesses_made + 1))
    while cur_guess not in word_set:
        cur_guess = input("invalid guess, try again: ")
    return cur_guess

def check_debug_flag(cur_guess):
    return cur_guess == "debug"

#this definitely isn't wordle

word_set = get_word_set()
word = list(word_set)[random.randint(0, len(word_set) - 1)]

guesses_made = 0
show_intro()

while guesses_made < 6:    
    cur_guess = get_valid_guess()

    
    
    if check_debug_flag(cur_guess):
        print(word)
        continue
    
    if cur_guess == word:
        print()
        print("you got it!")
        break
    else:
        print("wrong!")
    guesses_made += 1

            
    
    display = ["X", "X", "X", "X", "X"]
    word_temp = list(word)
    cur_guess = list(cur_guess)
    
    for i in range(len(word_temp)):
        if word_temp[i] == cur_guess[i]:
            word_temp[i] = "$" #dollar sign will be used as a placeholder 
            display[i] = "Y"
            cur_guess[i] = "$"

    for i in range(len(cur_guess)):
        if cur_guess[i] != "$" and cur_guess[i] in word_temp:
            display[i] = "S"
            cur_guess[i] = "$"
        elif display[i] == "X":
            display[i] = "N"
    print(display)
    print()
    
if guesses_made >= 6:
    print("you ran out of guesses!")
















