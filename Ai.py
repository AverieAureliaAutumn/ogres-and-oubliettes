import random
import csv

class Ai():
    def __init__(self, name, lastName, health):
        self.name = name
        health = random.randrange(50)


nameArray = ["Bob", "Steve", "Gill", "Wizzo", "Arthur"]
lastnameArray = ["The Weird", "The Wizard", "The Crazy", "The Evil", "The Loyal"]
for x in range(5):
    name = nameArray[random.randrange(0, len(nameArray), 1)]
    lastName = lastnameArray[random.randrange(0,len(lastnameArray),1)]
    health = random.randrange(50)
    print(name, lastName,":", str(health) + ":HP")
