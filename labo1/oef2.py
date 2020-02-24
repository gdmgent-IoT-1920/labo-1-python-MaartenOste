count = {}

f = open("namen.txt", "r")

temp = f.read().splitlines()

f.close()

for x in temp:
	if x not in count:
		count[x] = 1
	else:
		count[x] = count[x] +1

for x in count:
	print(x, end=': ')
	print(count[x])