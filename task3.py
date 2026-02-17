"""
Rectangular Prism Object
Create a class that creates a rectangular prism.  You should be able to set all of the important measurements (l,w,h) when the object is instantiated in the constructor and you should have class methods that determine the surface area and volume.
You should have class methods that also allow you to change the dimensions of the object.
Instantiate 3 separate rectangular prisms with the test data given, and check the assertions are correct.
"""
import math
class rectPrism:

    def getmeasurements(self):
        try: 
            self.l = self.kw['l']
            self.w = self.kw['w']
            self.h = self.kw['h']
            if self.l > 0 and self.w > 0 and self.h > 0:
                pass
            else:
                print("That is not a valid rectangle")
                self.go = False
                return
        except: 
            done = False
            while done == False:
                w = input("Enter width: ")
                l = input("Enter length: ")
                h = input("Enter height: ")
                if l.isnumeric() and w.isnumeric() and h.isnumeric():
                    self.l = l 
                    self.w = w
                    self.h = h
                    done = True 
                else:
                    print("Please re-enter measurements")
        

    def volume(self):
        if self.go != False:
            self.v = self.h*self.l*self.w
            return self.v
        else:
            return None
    def surfaceArea(self):
        if self.go != False:
            h = self.h
            l = self.l
            w = self.w
            self.sa = 2*(l*w+l*h+h*w)
            return self.sa
        else: 
            return None
    def __init__(self,**kwargs):
        self.kw = kwargs
        self.go = True
        self.getmeasurements()

        pass
# class instances and assertions below:

a = rectPrism(l=10,w=2,h=5)
assert a.volume() == 100
assert a.surfaceArea() == 160

b = rectPrism(l=1,w=1,h=1)
assert b.volume() == 1
assert b.surfaceArea() == 6

c = rectPrism(l=2,w=0,h=10)
# note the invalid width
assert c.volume() == None
assert c.surfaceArea() == None