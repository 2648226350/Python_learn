#3-8
destinations = ["the great wall","tibet","paris","london","shangrila"]

for destination in destinations:
    print(destination.title().ljust(16),end = "")
print()

for destination in sorted(destinations): #sorted not change the order eternal
    print(destination.title().ljust(16),end = "")
print()

destinations.reverse() #reverse will change the order eternal
for destination in destinations:
    print(destination.title().ljust(16),end = "")
print()

destinations.sort() #sort will change the order eternal
for destination in destinations:
    print(destination.title().ljust(16),end = "")
print()
#3-9
print(destinations.__len__())
#3-10
"""Try these functions freely!"""
#3-11
"""Deliberately cause some errors!"""