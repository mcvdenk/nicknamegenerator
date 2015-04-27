import random

namesfile = open('nicknames.txt','r')
names = []
for name in namesfile:
	names.append(name)
selected = ""
while (selected == ""):
	selected = names[random.randrange(len(names))].replace("\n","")
print(selected)
