#!/usr/bin/env python3

 
def shapes():
    import math
    while True:
        choose = input("Choose a shape (triangle, rectangle, circle). q quits:")
        
        if choose == "q":
            break;

        if choose in ['triangle','TRIANGLE','Triangle']:
            base = input("Give base of the triangle:")
            height = input("Give height of the triangle:")
            area =0.5*float(base)*float(height)    
            print("The area is","%2f" %area)
    
        elif choose in ['rectangle','RECTANGLE','Rectangle']:
            width = input("Give width of the rectangle:")
            height = input("Give height of the rectangle:")
            area =float(width)*float(height)
            print("The area is","%2f" %area)  
    
        elif choose in ['circle','CIRCLE','Circle']:
            radius = input("Give radius of the circle:")
            area =(float(radius)**2)*3.14159265358979323846
            print("The area is","%2f" %area)

        else:
            print("Unknown shape! Try again!")
def funny():
    import random
    print("Funny shape fact:\n")
    Funnyinfo =[
            "The first theorems relating to circles are attributed to Thales around 650 BC",
            "A triangle is the sign for God, Jesus and The Holy Spirit in christianity",
            "A rectangle is the most common shape for a rug",
            "Infants prefere circles to other shapes"]
    print(random.choice(Funnyinfo))
        
    reply =input("Interesting, right?")
    if input== "ok":
        ui()
    else:
        ui()
    

def stat():
    print("No stats so far")
    
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
            stat()
        elif ask =="f":
            funny()
        else:
            print("Unknown input")
            continue
            

                     
        

def main():
    ui()

main()