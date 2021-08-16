#3-4
guests = ["dante","vergil","nero"]
message = "would you like have dinner with me?"
for guest in guests:
    print("Hi "+guest.title()+", "+message)
#3-5
absentees = guests[1]
guests[1] = "v"
message_1 = " can't attend my dinner, but fortunately "
message_2 = " will represent him."
print(absentees.title()+message_1+guests[1].title()+message_2)
#3-6
message_3 = "I just found a bigger table! So I want to invite more friends! ^-^"
print(message_3)
guests.insert(0,"tresh")
guests.insert(int(guests.__len__()/2),"lady")
guests.append("jack")
for guest in guests:
    print("Hi "+guest.title()+", "+message)
#3-7
message_4 = "What a pity! I just know that the new table cannot be delivered in time. T-T"
print(message_4)
message_5 = "let's have dinner next time."
message_6 = "Please have dinner with me this weekend,"
while(int(guests.__len__()) > 2):
    guest = guests.pop(0)
    print("Sorry, "+guest.title()+" "+message_5)
for guest in guests:
    print(message_6+" "+guest.title()+" .")
