#8-12
def add_ingredient(*ingres):
    print("This sandwith contians: ")
    for ingre in ingres:
        print("- "+ingre)
add_ingredient('banana','pizza','cheese')
#8-13
def build_profile(family_name, given_name, **user_info):
    profile = {}
    profile[given_name] = family_name
    for key, val in user_info.items():
        profile[key] = val
    return profile
user_profile = build_profile('evence','lucien',
                              age  = '21',
                              city = 'alto',
                              rank = 'legend',)
for key, val in user_profile.items():
    print(key.title()+' '+val.title())
#8-14
def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info
car = make_car('subaru','outback',
                color = 'red',
                tow_package = True)
print(car)
