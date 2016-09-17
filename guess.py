import random
compNum=random.randint(0,10)

while True:
	userGuess=int(raw_input("Choose a number: "))
	if userGuess > compNum:
		print("Choose a smaller number")
		
	elif userGuess < compNum:
		print("Choose a bigger number")
		
	else:
		print("Hey, you chose the same number as the computer!")
		break


