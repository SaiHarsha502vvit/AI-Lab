from collections import defaultdict
import math
def solveWaterjug(amt1, amt2):
    if (amt1 == goal and amt2 == 0) or (amt2 == goal and amt1 == 0):
        print(amt1, amt2)
        return True
    if visited[(amt1, amt2)] == False:
        print(amt1, amt2)
        visited[(amt1, amt2)] = True
        return (solveWaterjug(0, amt2) or
                solveWaterjug(amt1, 0) or
                solveWaterjug(firstjug, amt2) or
                solveWaterjug(amt1, secondjug) or
                solveWaterjug(amt1 + min(amt2, (firstjug-amt1)),
                amt2 - min(amt2, (firstjug-amt1))) or
                solveWaterjug(amt1 - min(amt1, (secondjug-amt2)),
                amt2 + min(amt1, (secondjug-amt2))))
    else:
        return False
def check():
    if (firstjug <= goal) and (secondjug <= goal):
        print("Not Possible")
        return True
    elif (firstjug / 2 == secondjug or secondjug / 2 == firstjug) and (firstjug != goal and secondjug != goal):
        print("Not Possible")
        return True
    elif(goal % (math.gcd(firstjug, secondjug)) != 0):
        print("Not Possible")
        return True
firstjug = int(input("enter the firstjug value "))
secondjug = int(input("enter the secondjug value "))
goal = int(input("enter the goal value of the jug "))
visited = defaultdict(lambda: False)

result = check()
if result != True:
    print("Steps: ")
    solveWaterjug(0, 0)

