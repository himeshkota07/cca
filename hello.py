import random
print("Welcome to the guessing game")
n=random.random(100)
win=False
attempts=0
while(attempts<=5):
  guess=int(input("Guess the number between 0 to 100: "))
  attempts+=1
  if(n==guess):
    print("Correct guess.You won!")
    win=True
  else:
    print("Try again😊!")

if(win==False):
  print("You lost the game. Better luck next time")
