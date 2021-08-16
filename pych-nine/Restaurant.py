class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("This is "+self.restaurant_name.title()+
        " restaurant in "+self.cuisine_type.title()+" style.")
    def open_restaurant(self):
        print("The restaurant is opening.")