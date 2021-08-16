#9-13
from collections import OrderedDict
glossaries = OrderedDict()
glossaries['ascend'] = 'travel up'
glossaries['envisage'] = 'form a mental image of sth'
glossaries['versatile'] = 'having great diversity or variety'
glossaries['atlas'] = 'a collection of maps in book form'
glossaries['exaggeration'] = 'the act of making sth more noticeable than usual'
glossaries['concise'] = 'expressing much in few words'
for glossary,mean in glossaries.items():
    print(glossary+": "+mean)
#9-14
from random import randint
class Die():
    def __init__(self,sides = 6):
        self.sides = sides
    def roll_die(self):
        print(str(self.sides)+"sides: "+str(randint(1,self.sides)))
six = Die(6)
ten = Die(10)
twenty = Die(20)
for i in range(1,11):
    six.roll_die()
#9-15
"""Python Module of the Week:http://pymotw.com/"""