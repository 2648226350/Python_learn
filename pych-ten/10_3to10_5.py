#10-3
filename = 'pych-ten/guest.txt'
with open(filename,'w') as file_object:
    file_object.write("dante\nnaruto")
#10-4
name = input("Please input your name: ")
while name != 'quit':
    print("Hello, "+name.title())
    filename_2 = 'pych-ten/guest_book.txt'
    with open(filename_2,'a') as file:
        file.write(name.title()+'\n')
    name = input("Please input your name: ")
#10-5
reason = input("Why do you like coding? ")
while reason != 'quit':
    filename_3 = 'pych-ten\\reason.txt'
    with open(filename_3,'a') as file:
        file.write(reason+"\n")
    reason = input("Why do you like conding? ")