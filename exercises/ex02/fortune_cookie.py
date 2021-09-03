"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730236986"

from random import randint
print("Your fortune cookie says... ")

MESSAGE: int = randint(1, 4)
   
if MESSAGE == 1:
    print("You will be called in to fulfill a position of high honor and responsibility.") 
else:
    if MESSAGE == 2:
        print("You learn from your mistakes... You will learn a lot today.")
    else: 
        if MESSAGE == 3:
            print("Life consists not in holding good cards, but in playing those you hold well.")
        else:
            if MESSAGE == 4:
                print("The greatest love is self-love.")            

print("Now, go spread positive vibes! ") 