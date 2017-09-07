#!/Library/Frameworks/Python.framework/Versions/3.6/bin

import sys
import random
assert sys.version_info >= (3,4), "This script requires at least Python 3.4"

guessesTaken = 0
maxGuesses = 5
numRange = 30

print("Welcome to Guess the Number")
print("I'm thinking of a number between 1 and 30")
print("You have 5 attempts to guess the correct number")

number = random.randint(1,numRange)

for guessesTaken in range(maxGuesses):
	guess = input('Guess the number: ')
	try:
		guess = int(guess)
		if guess < number:
			print("close, but too low")
		if guess < number - 5:
			print("too low")
		if guess > number:
			print("close, but too high")
		if guess > number + 5:
			print("too high")
		if guess == number:
			break

	except ValueError:
		print("please enter a valid integer")

if guess == number:
	guessesTaken = str(guessesTaken + 1)
	print('Well done, you guessed the number in '+ guessesTaken +' attempts')

if guess != number:
	number = str(number)
	print('You are out of attempts. The number I was thinking of was ' + number + '.')

