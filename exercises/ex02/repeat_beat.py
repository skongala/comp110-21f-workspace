"""Repeating a beat in a loop."""

__author__ = "730236986"

beat: str = (input("What beat do you want to repeat? "))
REPEAT: int = int(input("How many times do you want to repeat it? ")) 

i: int = 0
if REPEAT <= i: 
    print("No beat...")
while REPEAT > i:
    print(str(beat + " ") * REPEAT)
    REPEAT = REPEAT * 0