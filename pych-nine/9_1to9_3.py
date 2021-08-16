#9-1
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("This is "+self.restaurant_name.title()+
        " restaurant in "+self.cuisine_type.title()+" style.")
    def open_restaurant(self):
        print("The restaurant is opening.")
restaurant = Restaurant('michelin','chinese')
print("The restaurant called: "+restaurant.restaurant_name.title())
print("The style of this restaurant is "+restaurant.cuisine_type.title())
restaurant.describe_restaurant()
restaurant.open_restaurant()
#9-2
busgirl = Restaurant('busgirl','amercian')
meet = Restaurant('meet','italian')
busgirl.describe_restaurant()
meet.describe_restaurant()
#9-3
class User():
    def __init__(self,given_name,family_name,email):
        self.given_name = given_name
        self.family_name = family_name
        self.email = email
    def describe_user(self):
        print("Name: "+self.given_name.title()+" "+self.family_name.title()+"\nE-mail: "+self.email)
    def greet_user(self):
        print("Hello, "+self.given_name.title()+" "+self.family_name.title()
                +", welcome to user xxxxx.")
wicher = User('evence','lucien','2648226350@qq.com')
wicher.describe_user()
wicher.greet_user()