inp = input("Type een zin die je wenst om te draaien: ") 

out = inp.split(" ")
out.reverse()

print('Omgedraaid:')
for x in range(len(out)):
  print(out[x], end = ' ')