#6-7
info_one = {'family_name':'evans',
            'given_name':'lucian',
            'age':'21',
            'city':'alto',}
info_two = {'family_name':'hofenberge',
            'given_name':'natasha',
            'age':'23',
            'city':'alingham',}
info_thr = {'family_name':'karendia',
            'given_name':'rhine',
            'age':'151250',
            'city':'observer castle',}
people = [info_one,info_two,info_thr]
for info in people:
    print("\n")
    for key, val in info.items():
        print(key.title()+": "+val.title())
#6-8
toby = {'class':'dog',
        'master':'jack',}
miya = {'class':'cat',
        'master':'alice',}
ciel = {'class':'dog',
        'master':'petter',}
nana = {'class':'cat',
        'master':'lance',}
pets = [toby,miya,ciel,nana]
for pet in pets:
    print("\n")
    for key, val in pet.items():
        print(key.title()+": "+val.title())
print()
#6-9
p_one = ["the great wall","the himalayas","the forbidden city"]
p_two = ["the mount fuji","the tai mahal","the angkor wat"]
p_thr = ["the suez canal","the sahara desert","the pyramids"]
favorite_places = {'dante':p_one,
                   'vergil':p_two,
                   'nero':p_thr,}
for key, val in favorite_places.items():
    print(key.title()+"'s faverite places contains:")
    for place in val:
        print(place.title().ljust(20),end = "")
    print()
print()
#6-10
"""Similar with 6-9,replace the faverite places with faverite number"""
#6-11
info_one = {'country':'china',
            'population':'524w',
            'fact':'Peking is both the economy and politics center of China.',}
info_two = {'country':'france',
            'population':'131w',
            'fact':'Paris is known as the "Romantic Tity","Fashion City".',}
info_thr = {'country':'england',
            'population':'213w',
            'fact':'London is the capital of Britain.',}
cities = {'peking':info_one,
          'paris':info_two,
          'london':info_thr,}
for city, infomation in cities.items():
    print("Name: "+city.title())
    for key, val in infomation.items():
        print(key.title()+": "+val.title())
    print()
#6-12
"""Try to expand some examples."""