#9-4
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print("This is "+self.restaurant_name.title()+
        " restaurant in "+self.cuisine_type.title()+" style.")
    def open_restaurant(self):
        print("The restaurant is opening.")
    def set_number_served(self,num):
        if num < self.number_served:
            print("Error!")
        else:
            self.number_served = num
    def increment_number_served(self,incre):
        self.number_served += incre
restaurant = Restaurant('miche','chinese')
print("Day Zero:")
print("There are "+str(restaurant.number_served)+" people have eaten in the restaurant.")
restaurant.set_number_served(2000)
print("Day Ten:")
print("There are "+str(restaurant.number_served)+" people have eaten in the restaurant.")
restaurant.increment_number_served(300)
print("Day Twelve:")
print("There are "+str(restaurant.number_served)+" people have eaten in the restaurant.")
#9-5
class User():
    def __init__(self,given_name,family_name,email):
        self.given_name = given_name
        self.family_name = family_name
        self.email = email
        self.login_attempts = 0
    def describe_user(self):
        print("Name: "+self.given_name.title()+" "+self.family_name.title()+"\nE-mail: "+self.email)
    def greet_user(self):
        print("Hello, "+self.given_name.title()+" "+self.family_name.title()
                +", welcome to user xxxxx.")
    def incre_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
user_1 = User('lucien','evence','2648226350@qq.com')
login = input("Do you want to login? ")
while login.lower() == 'yes':
    user_1.incre_login_attempts()
    print(user_1.login_attempts)
    login = input("Do you want to login? ")
user_1.reset_login_attempts()
print(user_1.login_attempts)
