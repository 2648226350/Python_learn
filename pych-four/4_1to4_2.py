#4-1
pizzas = ["new york style","chicago style","california style","pan pizza"]
for pizza in pizzas:
    print(pizza.title().ljust(20),end = "")
print()
comment = "I like "
for pizza in pizzas:
    print(comment+pizza.title()+".")
summary = "I really love pizza!"
print(summary)
#4-2
animals = ["lion","dog","cat","tigger"]
feature = "likes eat meat."
for animal in animals:
    print(animal.title()+" "+feature)
common_ground = "Any of these animals likes eat meat."
print(common_ground)
