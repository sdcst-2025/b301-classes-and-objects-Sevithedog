import random
import os
class game:
    def showTitle(self):
        # clear console and show instructions
        os.system("clear||cls")
        print("Welcome to the number guessing game!")
        print("I will pick a secret number from 1 to 100. You must guess it!")

    def generateSecret(self):
        #generates random number from 1-100
        self.randN = random.randint(1,100)

    def getGuess(self):
        #get the users's guess
        while True:
            try:
                g = int(input("Enter your guess. It should be an integer: "))
                if 1 <= g <= 100:
                    break
            except:
                print("That is not a valid input. Try again.")
                pass
        self.guess = g

    def compareGuess(self):
        #return result as 0 for equal, -1 for low, 1 for hight
        a = self.guess
        b = self.randN
        self.result = 0 if a==b else (1 if a > b else -1)

    def showMessage(self):
        #show message about accuracy of guess
        self.compareGuess()
        messages = {
            -1: "That guess is too low",
            0 : "Correct!",
            1 : "Your guess is too high"
        }
        print(messages[self.result])

    def __init__(self):
        self.showTitle()
        self.generateSecret()
        numberOfGuesses = 0
        while True:
            self.getGuess()
            numberOfGuesses += 1
            self.showMessage()
            if self.result == 0:
                break
        print(f"Congratulations! You guessed the secret number in {numberOfGuesses} tries")

play = game()