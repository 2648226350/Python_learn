#9-6
from Restaurant import Restaurant
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,*flavors):
        super(IceCreamStand,self).__init__(restaurant_name,cuisine_type)
        self.flavors = flavors
    def output(self):
        for flavor in self.flavors:
            print(flavor.title().ljust(30),end = "")
        print()
icecream = IceCreamStand('SAO','versatile','cookie dough','phish food','strawberry chessecake')
icecream.output()
icecream.open_restaurant()
icecream.describe_restaurant()
#9-7
from User import User
class Admin(User):
    def __init__(self,given_name,family_name,email,*privileges):
        super(Admin,self).__init__(given_name,family_name,email)
        self.privileges = privileges
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege.title().ljust(30),end = "")
        print()
jack = Admin('dante','spadar','none','can add post','can delete post','can ban user')
jack.show_privileges()
#9-8
class Privileges():
    def __init__(self,privileges = ['can add post','can delete post','can ban user']):
        self.privileges = privileges
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege.title().ljust(30),end = "")
        print()
class Admin(User):
    def __init__(self,given_name,family_name,email):
        super(Admin,self).__init__(given_name,family_name,email)
        self.privileges = Privileges()
jack = Admin('dante','spadar','none')
jack.privileges.show_privileges()
#9-9
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has "+str(self.battery_size)+" -kWh battery.")
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
audo = Battery()
audo.describe_battery()
audo.upgrade_battery()
audo.describe_battery()