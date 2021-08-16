#7-1
car = input("What car do you want to rent? ")
message = "Let me see if I can find you a "
print(message+car.title()+".")
#7-2
person_num = int(input("How many of you are there for dinner? "))
if person_num > 8:
    print("Sorry, we have no spare table already.")
else:
    print("Ok, we have enough table now.")
#7-3
number = int(input("Please input a number: "))
if number % 10:
    print("The number is not the multiple of 10.")
else:
    print("The number is the multiple of 10.")

