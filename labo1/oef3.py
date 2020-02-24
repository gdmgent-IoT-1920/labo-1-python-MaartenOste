import random

number  = random.randrange(1000, 10000)

number = str(number)

inp = ''
counter = 0

print("LINGO-BINGO Welkom bij het kip en eieren spel!")

while inp != number:
	correct = 0
	contains = 0
	if counter != 0:
		i=0
		for x in number:
			if number[i] == inp[i]:
				correct+=1
			if number[i] in inp and number[i] != inp[i]:
				contains+=1
			i+=1
		if correct == 1:
			print(str(correct) + " kip", end=', ')
		else:
			print(str(correct) + " kippen", end=', ')
		if contains == 1:
			print(str(contains) + " ei")
		else:
			print(str(contains) + " eieren")
	inp = input("Geef een viercijferig nummer in: ") 
	counter+=1

print("Je hebt gewonnen! Pogingen: " + str(counter))
