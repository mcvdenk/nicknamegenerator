import random

namesfile = open('nicknames.txt','r')
names = []
for name in namesfile:
	names.append(name)
selected = names[random.randrange(len(names))].replace("\n","")
if (selected != ""): print(selected)
