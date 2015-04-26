import random

namesfile = open('nicknames.txt','r')
names = []
for name in namesfile:
	if (name != ""): names.append(name)
selected = names[random.randrange(len(names))].replace("\n","")
print(selected)
