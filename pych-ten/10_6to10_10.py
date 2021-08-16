#10-6&&10-7
print("Give me two number, and I'll plus them.")
while True:
    num_one = input("First num: ")
    if num_one == 'q':
        break
    num_two = input("Second num: ")
    if num_two == 'q':
        break
    else:
        try:
            summary = int(num_one) + int(num_two)
        except ValueError:
            print("Please input a NUMBER!!!")
        else:
            print(num_one+" + "+num_two+" = "+str(summary))
#10-8&&10-9
from file_read import read_file
filenames = ['pych-ten\\cats.txt','dogs.txt']
for filename in filenames :
    print(filename+": ")
    read_file(filename)
#10-10
line = "Row, row, row your boat"
print(line.count('row'))
print(line.lower().count('row'))
