#import the modules
import sys
import random

ans = True

while ans:
    question = raw_input("Dare-you tell the Truth and ask the magic 10 ball:(press enter to quit)")
    words = ["Chicken", "Dare You"]
    BetYou = ["BetYou One Dollar", "BetYou One Penny"]
    answers = random.randint(1,10)
    randword = random.randint(0,1)
    BetYou = random.randint(0,1)
    word = words[randword]
    BetYou = BetYou[randword]
    print(word)
    print(BetYou)
    if question =="":
        sys.exit()

    elif answers == 1:
        print"If Chicken,then eat ketchup"

    elif answers == 2:
        print"If Chicken,DareYou to hop on one foot"

    elif answers == 3:
        print"DareYou,Smell you feet"

    elif answers == 4:
        print"Laugh-out Loud"

    elif answers == 5:
        print"DareYou,Balance book on head,standing on one foot"

    elif answers == 6:
        print"Wiggle your Hips"

    elif answers == 7:
        print"Tap Your Toes"

    elif answers == 8:
        print"DareYou,Pick Your Nose"

    elif answers == 9:
        print"If Chicken,Eat a donut"

    elif answers == 10:
        print"Have fun"
