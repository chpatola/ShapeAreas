
from shapes import *

def stat():
    triangles = get_tri()
    rectangles = get_rec()
    circles = get_cir()

    #List where only the area of the shapes are saved
    triA =[]
    recA =[]
    circA=[]

    while True:
        Import re

        %matplotlib inline
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
            break;
        else:
            break;
