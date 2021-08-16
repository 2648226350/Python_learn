#4-3
for num in range(1,21):
    print(str(num).ljust(5),end = "")
print()
#4-4
"""print(1~1000000)"""
#4-5
million = [i for i in range(1,1000001)]
print("Min in million: "+str(min(million)))
print("Max in million: "+str(max(million)))
print("Sum of million: "+str(sum(million)))
#4-6
odd_number = [i for i in range(1,21,2)]
for num in odd_number:
    print(str(num).ljust(5),end = "")
print()
#4-7
multiple_of_three = [i for i in range(3,31,3)]
for num in multiple_of_three:
    print(str(num).ljust(5),end = "")
print()
#4-8
cube = [i**3 for i in range(1,11)]
for num in cube:
    print(str(num).ljust(5),end = "")
print()
#4-9
"""List parsing"""