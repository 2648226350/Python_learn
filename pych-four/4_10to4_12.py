#4-10
ninjas = ["uzumaki naruto","uchiha sasuke","haruno sakura","hatake kakashi",
            "nara shikamaru","sai","yamanaka lno","tsunade","yamato"]
print("The first three ninjas in the list are: ")
for ninja in ninjas[:3]:
    print(ninja.title())
print("Three ninjas form the middle of the list are: ")
for ninja in ninjas[int(len(ninjas)/2)-1:int(len(ninjas)/2)+2]:
    print(ninja.title())
print("The last three ninjas in the list are: ")
for ninja in ninjas[len(ninjas)-3:]:
    print(ninja.title())
#4-11
friend_ninjas = ninjas.copy()
friend_ninjas.append("hyuga hinata")
print("My favorite ninjas are: ")
for ninja in ninjas:
    print(ninja.title().ljust(30),end = "")
print()
print("My friend's favorite pizzas are: ")
for ninja in friend_ninjas:
    print(ninja.title().ljust(30),end = "")
print()
#4-12
"""Use multiple circulate"""
