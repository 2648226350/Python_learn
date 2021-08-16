#8-3
def make_shirt(size, words):
    print("This T-shirt is "+str(size)+" yards in size, and it was printed with '"+words+"'.")
make_shirt(34,'Warrios')
make_shirt(words = 'Rise',size = 55)
#8-4
def make_big_shirt(size, words = 'I love Python'):
    print("This T-shirt is "+str(size)+" yards in size, and it was printed with '"+words+"'.")
make_big_shirt(34)
#8-5
def describe_city(name, country = 'china'):
    print(name.title()+" is in "+country.title()+".")
describe_city('Peking')
describe_city('Changsha')
describe_city('London','england')