#7-8
sandwich_orders = ['pastrami','chicken','pastrami','corned-beff','pastrami']
finished_sandwiches = []
for sandwich_order in sandwich_orders:
    print("I made your "+sandwich_order+" sandwich")
    finished_sandwiches.append(sandwich_order)
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche+" sandwich")
#7-9
message = "Sorry, pastrami has been sold out."
print(message)
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
#7-10
place = input("If you could visit one place in the world, where woule you go?(input 'quit' to quit) ")
places = []
while place != 'quit':
    places.append(place)
    place = input("If you could visit one place in the world, where woule you go?(input 'quit' to quit) ")
for place in places :
    print(place.upper().ljust(20),end = "")
print()