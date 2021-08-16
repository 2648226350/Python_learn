#10-11&&10-12
import json

filename = 'pych-ten\\favorite_number.json'
try:
    with open(filename) as f_obj:
        f_num = json.load(f_obj)
except FileNotFoundError:
    favorite_num = input("Please tell me your favorite number,I'll remember it. ")
    with open(filename, 'w') as f_obj:
        json.dump(favorite_num, f_obj)
else:
    print("I konw your favorite number! It's "+f_num+".")
#10-13
"""None"""




