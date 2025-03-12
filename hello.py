import random
print("Welcome to the guessing game")
n=random.randint(100)
win=False
for i in range(5):
  guess=int(input("Guess the number between 0 to 100: "))
  if(n==guess):
    print("Correct guess.You won!")
    win=True
    return 0
  else:
    print("Try again😊!")
