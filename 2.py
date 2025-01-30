# Number guessing game 
from random import randint
def guess():
    x = randint(0,100)
    while True:
        try:
            b = int(input("Enter the number"))
            if(b != x):
                if(b> x):
                    print("Too high")
                else:
                    print("Too low")
            elif( b == x):
                print("You won")
                break        
        except:
            print("Invalid input")

guess()