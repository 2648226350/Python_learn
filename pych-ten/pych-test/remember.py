import json
username = input("What is your name? ")
filename = 'pych-test\\username.json'
with open(filename, 'a') as f_obj:
    json.dump(username.title()+"\n",f_obj)
print("We'll remember you when you come back, "+username.title())

