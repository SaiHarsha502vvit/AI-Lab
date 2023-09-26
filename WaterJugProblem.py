from collections import defaultdict
import math

jug1 = int(input("Enter the jug1 value: "))
jug2 = int(input("Enter the jug2 value: "))
aim = int(input("Enter the aim: "))

visited = defaultdict(lambda: False)

def waterJugSolver(amt1, amt2, action="Initial state"):
    print(f"{action}: Jug1: {amt1}, Jug2: {amt2}")
    
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(f"Goal reached: Jug1: {amt1}, Jug2: {amt2}")
        return True

    if visited[(amt1, amt2)] == False:
        visited[(amt1, amt2)] = True
        # Fill Jug1
        if amt1 < jug1:
            if waterJugSolver(jug1, amt2, action="Fill Jug1"):
                return True
        # Fill Jug2
        if amt2 < jug2:
            if waterJugSolver(amt1, jug2, action="Fill Jug2"):
                return True
        # Empty Jug1
        if amt1 > 0:
            if waterJugSolver(0, amt2, action="Empty Jug1"):
                return True
        # Empty Jug2
        if amt2 > 0:
            if waterJugSolver(amt1, 0, action="Empty Jug2"):
                return True
        # Pour from Jug1 to Jug2
        if amt1 > 0 and amt2 < jug2:
            transfer = min(amt1, jug2 - amt2)
            if waterJugSolver(amt1 - transfer, amt2 + transfer, action=f"Pour from Jug1 to Jug2 ({transfer} units)"):
                return True
        # Pour from Jug2 to Jug1
        if amt2 > 0 and amt1 < jug1:
            transfer = min(amt2, jug1 - amt1)
            if waterJugSolver(amt1 + transfer, amt2 - transfer, action=f"Pour from Jug2 to Jug1 ({transfer} units)"):
                return True
    
    return False

def check():
    if jug1 <= aim and jug2 <= aim:
        print("Not Possible")
        return True
    elif (jug1 / 2 == jug2 or jug2 / 2 == jug1) and (jug1 != aim and jug2 != aim):
        print("Not Possible")
        return True
    elif aim % (math.gcd(jug1, jug2)) != 0:
        print("Not Possible")
        return True

result = check()
if result != True:
    print("Steps:")
    waterJugSolver(0, 0)
