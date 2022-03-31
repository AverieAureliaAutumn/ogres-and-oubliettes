from Location import *
Start = Location("Campfire","You wake up near a campfire, in a unfamiliar place.")
Town = Location("Town","You find yourself near an entrance to the town. It is a dirt path that takes you straight to the inn")
Forest = Location("Forest","You explore the forest and find yourself in a strange place.\n The sounds of birds disappears, as everything around you seems to fade in mist.\n Magical blue mushrooms light the way, as you gently follow a trail lit; you make your way to a local inn.")
Inn = Location("Inn","You arrive at the Inn. A fireplace is burning, and the atmosphere is jolly")
Elune = Location("Elune","You arrive at a place indescribable.This is the realm of the gods")






startingLocation = Start
Start.connect(Town)
Start.connect(Forest)
Town.connect(Inn)
Forest.connect(Inn)
Elune.connect(Forest)

