#5-3 && 5-4 && 5-5
def judge_color(alien_color):
    if alien_color == "green":
        points = 5
    elif alien_color == "yellow":
        points = 10
    elif alien_color == "red":
        points = 20
    return points
alien_color = input("Please input 'red'||'greed'||'yellow' : ")
points = judge_color(alien_color)
print("You got "+str(points)+" points!")
#5-6
age = int(input("Please input a positive integer : "))
if age < 2:
    print("He is a baby.")
elif age < 4 and age >= 2:
    print("He is toddlering.")
elif age < 13 and age >= 4:
    print("He is a child.")
elif age < 20 and age >= 20:
    print("He is a teenager.")
elif age < 65 and age >= 20:
    print("He is a adult.")
else :
    print("He is an old man.")
#5-7
fruits = ["banana","peach","apple","pear","watermelon","cherry"]
favorite_fruits = ["peach","watermelon","cherry"]
for fruit in fruits:
    if fruit in favorite_fruits:
        print("You really like "+fruit+"!")
