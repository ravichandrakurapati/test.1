"""
i have a dice with the numbers 1 -6
if the total count of dice is 20 then win
if the total count is greater then 20 then lost"""
import random

def dice():
    return random.randint(1,6)
def play():
    roll=0
    while roll<20:
        roll+=dice()
        print(roll)
        if (roll==20):
            print("congratulations")
        elif(roll<20):
            pass
        else:
            print("lose the match")
play()
