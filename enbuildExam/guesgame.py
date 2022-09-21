# 2. Write a game to "Guess the number", that means your program will generate any random number and the user will need to guess the number. In this if take the input from the user
# - if user guesses the correct number (i.e. it is equal to the generated random number) then show him success message as "You have guessed the number " + number and if  
# - if user fails to guess then show message "Not a correct number please try again" and take the next number from the user


import random
import math

lower = int(input("Enter Lower bound:- "))


upper = int(input("Enter Upper bound:- "))


x = random.randint(lower, upper)
print("\n\tYou've only ",
	round(math.log(upper - lower + 1, 2)),
	" chances to guess the integer!\n")


count = 0


while count < math.log(upper - lower + 1, 2):
	count += 1

	
	guess = int(input("Guess a number:- "))

	
	if x == guess:
		print("Congratulations you did it in ",
			count, " try")
		
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")


if count >= math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")


