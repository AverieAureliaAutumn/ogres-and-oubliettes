import time
import Items
import World
#a = Items.Player()

playerPos = World.startingLocation

# b = Items.Player()

# b.illness()
# a.illness()
def movementParser(input):
    input = input.lower()
    match input:
        case "forward":
            return "forward"
        case "backward":
            return "backward"
        case "left":
            return "left"
        case "right":
            return "right"
        case _:
            return "o"


def Inventory(items):
    items.gold = 100
    items.sword = 1
    items.potion = 5
    print("You have:", items.gold, "GOLD,", items.sword, "METAL SWORDS,", items.potion, "HEALTH POTIONS")


str = input("Welcome to the RPG Please enter your name : ")
print("Welcome", str, "Are you ready to begin? Press Y if yes Press N if no")
str = input("")
if str == "N":
    print("Program closing... You died")
    time.sleep(1)
    quit()
if str == "Y":
    print("Ok, Let us begin")
    time.sleep(2)
while True:
    playerPos.printOutLocation()
    print("")
    str = input("")
    # if str == "Sleep":
    #     print("You sleep until you die of old age. GAME OVER!")
    #     time.sleep(5)
    #     quit()
    #     break
    #
    # if str == "Inventory":
    #     Inventory(Items)

    # if str == "Sit up":
    #     print("You sit up, In the distance you see a town or small village. \n You can chose to GO TO TOWN \n "
    #           "Or you can EXPLORE")
    destination = playerPos.travel(str)
    if destination is not None:
        playerPos=destination
    #if str == "GO TO TOWN":

    #     print("You walk to the town...")
    #     time.sleep(5)
    #     playerPos.printOutLocation()
    #
    #
    #
    # elif str == "EXPLORE":
    #
    #     time.sleep(5)

