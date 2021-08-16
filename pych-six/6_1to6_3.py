#6-1
information = { 'family_name':'lucian',
                'given_name':'evans',
                'age':'21',
                'city':'akato',}
for key,val in information.items():
    print(key+": "+val.title())
#6-2
favorate_nums = {'dante':'2',
                'vergil':'13',
                'nero':'1',
                'tresh':'5',
                'lady':'6',}
for key,val in favorate_nums.items():
    print(key.title()+"'s favorate num is "+val+".")
#6-3
glossary = {'riotous':'Unrestrained buy convention or morality',
            'subsidize':'Secure  the assistance of by granting a subsidy, as of nations or military forces',
            'incidence':'The relative frequency of occurrence of sth',
            'scratch':'An abraded area where the skin is torn or worn off',
            'undergo':'Pass through',}
for key, val in glossary.items():
    print("\n"+key+" :\n"+val)