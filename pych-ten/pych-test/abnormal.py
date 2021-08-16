from count_words import count_words
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divided by zero!")
print("Give me two nubers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    fi_num = input("First number: ")
    if fi_num == 'q':
        break
    se_num = input("Second number: ")
    if se_num == 'q':
        break
    try:
        answer = int(fi_num)/int(se_num)
    except ZeroDivisionError:
        print("You can't divided by zero!")
    else:
        print(answer)
filenames = ['pych-ten\\reason.txt','file\\hello.txt','pych-ten\\guest.txt','alice.txt',
            'pych-ten\\guest_book.txt','pych-ten\\learning_python.txt','README_inProject.md']
for filename in filenames:
    count_words(filename)
"""while True:
    fi_num = input("First number: ")
    if fi_num == 'q':
        break
    se_num = input("Second number: ")
    if se_num == 'q':
        break
    try:
        answer = int(fi_num)/int(se_num)
    except ZeroDivisionError:
        pass#now,it means python will do nothing while ZeroDivisionError happened
    else:
        print(answer)"""
