#!/usr/bin/env python3

from triangle import *
from circle import *
from rectangle import*

#Lists where all info about the shapes are saved
triangles =[]
rectangles =[]
circles =[]

def shapes():
    import math
    while True:
        choose = input("Choose a shape (triangle - t, rectangle - r, circle - c). q quits:")

        if choose == "q":
            break;

        if choose in ['triangle','TRIANGLE','Triangle','t']:
            base = input("Give base of the triangle:")
            height = input("Give height of the triangle:")
            area =0.5*float(base)*float(height)

            tri= Triangle(base,height,area)
            triangles.append(tri)

            print("The area is","%.2f" %area)

        elif choose in ['rectangle','RECTANGLE','Rectangle','r']:
            width = input("Give width of the rectangle:")
            height = input("Give height of the rectangle:")
            area =float(width)*float(height)

            rec= Rectangle(width,height,area)
            rectangles.append(rec)

            print("The area is","%.2f" %area)

        elif choose in ['circle','CIRCLE','Circle','c']:
            radius = input("Give radius of the circle:")
            area =(float(radius)**2)*3.14159265358979323846

            circ= Circle(radius,area)
            circles.append(circ)

            print("The area is","%.2f" %area)

        else:
            print("Unknown shape! Try again!")

#Functions for returning shape lists to be used by other functions
def get_tri():
    return triangles
def get_rec():
    return rectangles
def get_cir():
    return circles
