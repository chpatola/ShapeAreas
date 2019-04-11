#!/usr/bin/env python3

class Triangle:
    def __init__(self,base,height,area):
        self.base=base
        self.height=height
        self.area=area

    def area(self):
        return self.area


class Rectangle:
    def __init__(self,width,height,area):
        self.width=width
        self.height=height
        self.area=area

    def area(self):
        return self.area


class Circle:
    def __init__(self,radius,area):
        self.width=radius
        self.area=area

    def area(self):
        return self.area

#Lists where all info about the shapes are saved
triangles =[]
rectangles =[]
circles =[]

#List where only the area of the shapes are saved
triA =[]
recA =[]
circA=[]

def shapes():
    import math
    while True:
        choose = input("Choose a shape (triangle- t, rectangle - r, circle - c) . q quits:")

        if choose == "q":
            break;

        if choose in ['triangle','TRIANGLE','Triangle','t','T']:
            base = input("Give base of the triangle:")
            height = input("Give height of the triangle:")
            area =0.5*float(base)*float(height)

            tri= Triangle(base,height,area)
            triangles.append(tri)

            print("The area is","%.2f" %area)

        elif choose in ['rectangle','RECTANGLE','Rectangle','r','R']:
            width = input("Give width of the rectangle:")
            height = input("Give height of the rectangle:")
            area =float(width)*float(height)

            rec= Rectangle(width,height,area)
            rectangles.append(rec)

            print("The area is","%.2f" %area)

        elif choose in ['circle','CIRCLE','Circle','c','C']:
            radius = input("Give radius of the circle:")
            area =(float(radius)**2)*3.14159265358979323846

            circ= Circle(radius,area)
            circles.append(circ)

            print("The area is","%.2f" %area)

        else:
            print("Unknown shape! Try again!")
def funny():
    import random
    print("\nFunny shape fact: \n")
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
    import re
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAmount of calculations you have made so far:")
    print("\tTriangles: ",len(triangles))
    print("\tRectangles: ",len(rectangles))
    print("\tCircles: ",len(circles))

    print("\nAreas of your triangles:")
    for i in triangles:
        print("\t","%.2f" %i.area)
        ta= int(i.area)
        triA.append(ta)

    if len(triA) >1:
        t=plt.plot(triA,'mo')
        plt.title("Triangle areas")
        plt.ylabel("area")
        plt.xlabel("triangles")
        plt.xticks(range(0, len(triA)))
        plt.show(t)


    print("\nAreas of your rectangles:")
    for i in rectangles:
        print("\t","%.2f" %i.area)
        ra = int(i.area)
        recA.append(ra)

    if len(recA)>1:
        r=plt.plot(recA,'ro')
        plt.title("Rectangle areas")
        plt.ylabel("area")
        plt.xlabel("rectangles")
        plt.xticks(range(0, len(recA)))
        plt.show(r)

    print("\nAreas of your circles:")
    for i in circles:
        print("\t","%.2f" %i.area)
        ca = int(i.area)
        circA.append(ca)

    if len(circA)>1:
        c=plt.plot(circA,'ko')
        plt.title("Circle areas")
        plt.ylabel("area")
        plt.xlabel("circles")
        plt.xticks(range(0, len(circA)))
        plt.show(c)

    ready=input("Press any key to go back to the main menu")
    if re.match(r"[Oo][Kk]", ready):
        ui()
    else:
        ui()


def ui():
    goOn = True
    while goOn:
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
                goOn = False
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
