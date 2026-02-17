#!python3
"""
Compound Interest Calculator
Create a class object that accepts paramters for Principal, Annual Interest Rate, Number of compounding periods.  
Create a class method that calculates the amount of compound interest for a given length of time.

Extension: accept time given in different measurements, but convert them to years for use in your class template.
"""


class Calc:
    principal = 0
    rate = 0
    nPeriods = 0


    def getT(self):
        t =0
        if self.kwargs:
            il = self.kwargs['t'].split() 
        else: 
            it = input("Enter time in the following format: length of time space then one of (s,m,h,d,w,M,y) to signify the units. Eg 24 h")
            il = it.split()
        if il[1] == 's':
            t = float(il[0])/31536000
        elif il[1] == 'm':
            t = float(il[0])/525600
        elif il[1] == 'h':
            t = float(il[0])/8760
        elif il[1] == 'd':
            t = float(il[0])/365
        elif il[1] == 'w':
            t = float(il[0])/52
        elif il[1] == 'M':
            t = float(il[0])/12
        elif il[1] == 'y':
            t= float(il[0])
        return t 
    def interest(self,**kwargs):
        self.kwargs = kwargs
        t = self.getT()
        ins = self.p*(1+self.r/self.n)**(self.n*t) - self.p
        ins = round(ins,2)
        return ins
    
    def amount(self,**kwargs):
        self.kwargs = kwargs
        t = self.getT()
        a = self.p*(1+self.r/self.n)**(self.n*t)
        a = round(a,2)
        return a
    def __init__(self,P,r,n):
        self.p = P
        self.r = r/100
        self.n = n


a = Calc(P=1000,r=4,n=2)
assert a.interest(t ='3 y') == 126.16
assert a.amount(t= '5 y') == 1218.99

b = Calc(P=5000,r=5.25,n=12)
assert b.interest(t ='10 y') == 3442.62

