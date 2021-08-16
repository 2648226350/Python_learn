#5-8 && 5-9
user_names = ["admin","jack","dante","vergil","nero"]
if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print("Hello admin,would you like to see a status report?")
        else :
            print("Hello "+user_name.title()+", thank you for logging in again.")
else :
    print("We need to find some users!")
#5-10
current_users = ["sakura","naruto","sasuke","kakashi","hinata"]
new_users = ["sakura","naruto","jiraiya","gaara","kankuro"]
for n_user in new_users:
    if n_user.lower() in current_users:
        print("The user name has been used, please input another!")
    else :
        print("Set user name successfully!")
#5-11
nums = [i for i in range(1,11)]
for num in nums:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(str(num)+"th")

#5-12
"""Checking the way you setting if sentence"""
#5-13
"""Try to solve some practical problems with python."""


