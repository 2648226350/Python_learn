import output
#7-4
ingredient = input("Please input the ingredient that you want(input the 'quit' to quit). ")
while ingredient != "quit":
    print("We will add "+ingredient+" to your pizza.")
    ingredient = input("Please input the ingredient that you want(input the 'quit' to quit). ")
#7-5
age = int(input("How old are you? "))
while age > 0:
    if age < 3:
        cost = 0
    elif age>=3 and age<12:
        cost = 10
    else :
        cost = 15
    print("You need pay "+str(cost)+" dollars")
    age = int(input("How old are you? "))
#7-6
"""Try other ways to break the circulate."""
#7-7
someone = "You"
while someone == "You":
    output.right()









