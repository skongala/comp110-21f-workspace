"""EX01 numeric operators."""
__author__: str = "730236986"

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: ")) 

print((str(str(left) + " ** " + str(right) + " is " + str(left ** right))))
print(str(str(left) + " / " + str(right) + " is " + str(left / right)))
print(str(str(left) + " // " + str(right) + " is " + str(left // right)))
print(str(str(left) + " % " + str(right) + " is " + str(left % right)))