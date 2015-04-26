import random

namesfile = open('nicknames.txt','r')
names = []
for name in namesfile:
	names.append(name)
print(names[random.randrange(len(names))])
