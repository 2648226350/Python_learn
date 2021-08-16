#8-6
def city_country(name, country):
    print("'"+name.title()+", "+country.title()+"'")
city_country('Santiago', 'Chile')
city_country('Peking', 'China')
city_country('London', 'England')
#8-7
def make_album(singer, album, number = 0):
    if number != 0:
        return {singer:album,'number':number}
    else:
        return {singer:album}
print(make_album('Jach','Aaaa',3))
print(make_album('mj','Bbb'))
#8-8
singer = input("Please input the singer. ")
album = input("Please input the album. ")
while singer != 'quit':
    print(make_album(singer, album))
    singer = input("Please input the singer. ")
    album = input("Please input the album. ")
