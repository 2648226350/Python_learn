#'r' == reading 'w' == writing 'a' == add 'r+' == reading and writing
filename = 'file\hello.txt'
with open(filename,'w') as file:
    file.write("Hello world!\n")#it will clear hello.txt if this file exist!!!
with open(filename,'r') as file:
    print(file.read())
with open(filename,'a') as file:
    file.write("Hello Python!\n")#it will not clear
with open(filename,'r') as file:
    print(file.read().rstrip())
