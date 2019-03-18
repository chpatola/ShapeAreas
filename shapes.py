#!/usr/bin/env python3

import math

def main():
    # enter you solution here
    while True:
        choose = input("Choose a shape (triangle, rectangle, circle). q quits:")
        
        if choose == "q":
            break;

        if choose in ['triangle','TRIANGLE','Triangle']:
            base = input("Give base of the triangle:")
            height = input("Give height of the triangle:")
            area =0.5*float(base)*float(height)    
            print("The area is","%6f" %area)
    
        elif choose in ['rectangle','RECTANGLE','Rectangle']:
            width = input("Give width of the rectangle:")
            height = input("Give height of the rectangle:")
            area =float(width)*float(height)
            print("The area is","%6f" %area)  
    
        elif choose in ['circle','CIRCLE','Circle']:
            radius = input("Give radius of the circle:")
            area =(float(radius)**2)*3.14159265358979323846
            print("The area is","%6f" %area)

        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
