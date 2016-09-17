import random

while True:
  compTurn = random.randint(0,20)
  userTurn = int(raw_input("Pick a number between 1 and 20: "))
  if compTurn > userTurn:
    print("Pick a bigger number")
  elif compTurn < userTurn:
    print("Pick a lower number")
  else: 
    print("Correct!")
    break
