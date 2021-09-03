"""Counting letters in a string."""

__author__ = "730236986"

LETTER: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")

i: int = 0
count: int = 0
while i < len(word):
    word[i]
    if LETTER == word[i]: 
        count: int = count + 1
    i = i + 1
print("Count: " + str(count))
    