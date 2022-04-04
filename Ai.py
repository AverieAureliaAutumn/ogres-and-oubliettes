import random


class Ai():
    def __init__(self, name, lastName, health):
        self.name = name
        health = random.randrange(50)


nameArray = ["Bob", "Steve", "Gill", "Wizzo", "Arthur"]
lastnameArray = ["The Weird", "The Wizard", "The Crazy", "The Evil", "The Loyal"]
# for x in range(5):
#     name = nameArray[random.randrange(0, len(nameArray), 1)]
#     lastName = lastnameArray[random.randrange(0,len(lastnameArray),1)]
#     health = random.randrange(50)
#     print(name, lastName,":", str(health) + ":HP")
import csv
with open('names.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for x in range(5):
        #######################
        name = nameArray[random.randrange(0, len(nameArray), 1)]
        lastName = lastnameArray[random.randrange(0,len(lastnameArray),1)]
        health = random.randrange(50)
        print(name, lastName,":", str(health) + ":HP")
        #########################################
        writer.writerow([name, lastName, health])
