#3-1
names = ["alice","cecilia","claudia","desdemona","dante","vergil","nero"]
for name in names:
    print(name.title(),end=" ")
print()
#3-2
message_greet1 = "Hello "
message_greet2 = ",nice to meet you!"
for name in names:
    print(message_greet1+name.title()+message_greet2)
#3-3
vehicles = ["walk","bicycle","motorcycle","train","subway","air"]
declaration = "I would like to go out by "
for vehicle in vehicles:
    print(declaration+vehicle+".")