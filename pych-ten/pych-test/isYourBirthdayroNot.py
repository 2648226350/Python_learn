filename = 'file\pi_digits_million.txt'
with open(filename) as file:
    lines = file.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
birthday = input("Please input your bithday in the form of 'mmddyy': ")
if birthday in pi_string:
    print("Your birthday appears in the first hundred million digits of pi!")
else :
    print("Your birthday does not appear in the first hundred million digits of pi.")
