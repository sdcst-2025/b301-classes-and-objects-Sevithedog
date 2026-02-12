import os
class quadratic:
    def showInstructions(self):
        os.system("clear||cls")
        print("- Quadratic Equation Calculator - ")
        print("You will enter a quadratic in standard form")
        print("          ax² + bx + c")
        print("I will ask you for the coefficients")
        print("I will then tell you several things about the quadratic")
        print("I hope you are ready, this poop is about to get real!\n")

    def getCoeffs(self):
        vars = ['a','b','c']
        for i in range(3):
            while True:
                try:
                    coeff = int(input(f"Enter coefficient {vars[i]} >"))
                    vars[i] = coeff 
                    break
                except:
                    print("invalid! It must be an integer. Try again")

        self.a = vars[0]
        self.b = vars[1]
        self.c = vars[2]   

    def getVertex(self):
        a = self.a
        b=self.b
        c=self.c
        self.x = -(b)/(2*a)
        self.y = a*self.x**2 + b*self.x + c

    def getVertexForm(self):
        x = self.x
        y = self.y
        if x < 0:
            self.bracket = f"(x + {-1*x})"
        else:
            self.bracket = f"(x - {x})"
        if y < 0:
            self.constant = f"- {-1*y}"
        else:
            self.constant = f" + {y}"
        self.vertexForm= f"{self.a}{self.bracket}² {self.constant}"

    def getDiscriminant(self):
        a = self.a
        b =self.b
        c = self.c
        self.disc = b**2 - 4*a*c

    def getXInt(self):
        self.getDiscriminant()
        a = self.a
        b = self.b
        disc = self.disc
        self.roots = []
        if disc >= 0:
            r1 = round((-(b) + disc**(0.5))/(2*a),3)
            r2 = round((-(b) - disc**(0.5))/(2*a),3)
            self.roots.append(r1)
            self.roots.append(r2)
        else:
            self.roots.append('non real')
            self.roots.append('non real')

    def __init__(self):
        #show instructions
        self.showInstructions()
        #ask user for coefficients
        self.getCoeffs()
        self.getVertex()
        print(self.x,self.y)
        self.getVertexForm()
        print(self.vertexForm)
        yint = self.c
        print(yint)
        self.getXInt()
        print(self.roots)
        #determine vertex form of parabola
        #determine directino of opening
        #determine y-intercept
        #determine x-intercepts (if they exist)
run = quadratic()