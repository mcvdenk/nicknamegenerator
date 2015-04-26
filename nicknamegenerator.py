import random

namesfile = open('nicknames.txt','r')
names = []
for name in namesfile:
	if (name.isalpha()): names.append(name).replace("\n","")
selected = names[random.randrange(len(names))].replace("\n","")
print(selected)
