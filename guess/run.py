'''
Copyright © 2022 AzizbekDeveloper
https://www.azizbekdeveloper.herokuapp.com/ - Website
https://www.instagram.com/azizbekdeveloper/ - Instagram
'''
START = "\
Copyright © 2022 AzizbekDeveloper\n\n\
https://www.azizbekdeveloper.herokuapp.com/ - Website\n\
https://www.instagram.com/azizbekdeveloper/ - Instagram"
print(START)
import random
SCORE = {
    "you":0,
    "me":0
}
def calculate_score():
    if SCORE["me"] > SCORE["you"]:
        return f"I'm win😌. Your score is {SCORE['you']}, my score is {SCORE['me']}"
    elif SCORE["me"] < SCORE["you"]:
        return f"Not bad. You win.😇. Your score is {SCORE['you']}, my score is {SCORE['me']}"
    else:
        return f"Nice Draw😀 Your score is {SCORE['you']}, my score is {SCORE['me']}\n I want to play again. Lets play"
def guess(x: "int"):
    random_number = random.randint(1, x)
    g = 0
    while g != random_number:
        g = int(input(f"Guess a number between 1 and {x}: "))
        if g < random_number:
            print(f"Guess again, too low.")
        elif g > random_number:
            print(f"Guess again, too high.")
        else:
            SCORE["you"] += 1
            print(f"Greast, You have guessed the number {random_number} correctly🤩!!!")
       
def computer_guess(x):
    try:

        low = 0
        high = x
        feedback = ''
        while feedback != "c":
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = low
            feedback = input(f"Is {guess} too high (H), too low(L), or correct (C)").lower()
            if feedback == 'h':
                high = guess -1
            elif feedback == 'l':
                low = guess + 1
        SCORE["me"] += 1
        print(f"Nice. I have guessed your number correctly🤘!!!, {guess}")
    except:
        print("You are cheating😠...")

while True:
    start_line = "\nEnter (C) -> The computer tries to guess.\nEnter (I) -> You try to guess the computer.\nEnter (q) or (e) for exit."
    print(start_line)
    inp = input("$: ").lower()
    if inp == "e" or inp == "q":
        break
    if inp == "c":
        x = int(input("Enter a number limit to estimate. Ex.: 10 $: "))
        computer_guess(x)
        print(calculate_score())
    elif inp == "i":
        x = int(input('Enter a number limit to estimate. Ex.: 10 $: '))
        guess(x)
        print(calculate_score())
    else:   
        print(start_line)