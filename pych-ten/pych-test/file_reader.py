with open('file\pi_thirty.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
filename = 'file\pi_thirty.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
pi_string = ""
for line in lines:
    pi_string += line.strip()
print(pi_string+"...")
