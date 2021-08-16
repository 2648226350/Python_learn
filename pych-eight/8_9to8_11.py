#8-9
magicians = ['liuqian','robert','jasper','lance']
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title().ljust(20),end = "")
    print()
show_magicians(magicians)
#8-10
def make_great(magicians):
    magicians_great = []
    for i in range(0,len(magicians)):
        magicians_great.append("the Great "+magicians[i].title())
    return magicians_great
magicians_great = make_great(magicians)
show_magicians(magicians_great)
#8-11
show_magicians(magicians)