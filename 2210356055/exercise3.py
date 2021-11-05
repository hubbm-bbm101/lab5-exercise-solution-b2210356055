import random

random_number = random.randint(1 , 100)
print("i picked up a number from 1 to 100")
user_guess = int(input("guess what is: "))
while user_guess != random_number:
	if user_guess < random_number:
		print("increase your number")
	elif user_guess > random_number:
		print("decrease your number")
	user_guess = int(input("guess what is: "))
print("You won. The number is {}".format(random_number))