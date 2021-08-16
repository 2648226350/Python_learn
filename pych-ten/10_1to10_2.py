#10-1
filename = 'pych-ten\learning_python.txt'
with open(filename) as file:
    print(file.read().rstrip())
print()
with open(filename) as file:
    for fil in file:
        print(fil.rstrip())
print()
with open(filename) as file:
    strings_learn = file.readlines()
for string_learn in strings_learn:
    print(string_learn.rstrip())
print()
#10-2
with open(filename) as file:
    contents = file.read().replace('Python','C')
    print(contents)