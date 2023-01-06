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
        if cur_guess == debug_keyword:
            break
        cur_guess = input("invalid guess, try again: ")
        
    return cur_guess

def check_debug_flag(cur_guess):
    if cur_guess == debug_keyword:
        print("Word: " , word)
        print()
    return cur_guess == debug_keyword

def update_display(word, guess):
    word_temp = list(word)
    cur_guess = list(guess)
    
    display = ["X", "X", "X", "X", "X"]
    
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
    return display
    
def show_display(display):
    print(display)
    print()
    
#this definitely isn't wordle

debug_keyword = "debugger"

word_set = get_word_set()
word = list(word_set)[random.randint(0, len(word_set) - 1)]

guesses_made = 0
show_intro()

while guesses_made < 6:    
    cur_guess = get_valid_guess()
    
    if check_debug_flag(cur_guess):
        continue
    
    if cur_guess == word:
        print()
        print("you got it!")
        break
    else:
        print("wrong!")
    guesses_made += 1

    display = update_display(word, cur_guess)
    show_display(display)
    
if guesses_made >= 6:
    print("you ran out of guesses!")
















