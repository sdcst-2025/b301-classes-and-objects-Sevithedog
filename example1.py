#!python3

# Example of a class template and an instantiated object
import math

class circle:
    radius = 0
    diameter = 0
    
    def calcDiameterToRadius(self):
        self.radius = self.diameter / 2
    
    def calcRadiusToDiameter(self):
        self.diameter = self.radius * 2

    def setRadius(self,value):
        self.radius = value
        self.calcRadiusToDiameter()

    def setDiameter(self,value):
        self.diameter = value
        self.calcDiameterToRadius()
    
    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return math.pi * self.diameter 
    
    def __init__(self,r=0,d=0):
        if r > 0:
            self.radius = r
            self.calcRadiusToDiameter()
        elif d > 0:
            self.diameter = d
            self.calcDiameterToRadius()
        else:
            print("No valid radius or diameter defined.  Radius or diameter needs to be set.")
    
    def __del__(self):
        print("this object destroyed")
    

a = circle(r=-1)
print( a.area() )