
from shapes import *
from funny import *
from statt import *

def ui():

    while True:
        ask=input("""\n***** This is a programme for calculating areas of shapes *****\n
        What do you want to do? \n
        Press...\n
        c to -> Calculates areas for shapes\n
        s for -> Statistics\n
        f for -> Funny shape info\n
        q to quit """)

        if ask =="q":
            sure = input("Are you sure you want to quit? y/n")
            if sure == "y":
                break
            else:
                continue
        elif ask =="c":
            shapes()
        elif ask =="s":
            statt()
        elif ask =="f":
            funny()
        else:
            print("Unknown input")
            continue
