#6-4
"""Equal with 6-3"""
#6-5
rivers = {"amazon":"brazil",
          "nile":"egypt",
          "yangtze":"china",
          "mississippi":"american",
          "yellow":"china",}
for key, val in rivers.items():
    print("The "+key.title()+" River runs through "+val.title()+".")
print()
#6-6
favorite_languages = {'jen':'python',
                      'sarah':'c',
                      'edward':'ruby',
                      'phil':'rust',}
for name, language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+language.title()+".")
respondents = ["sarah","vargil","naruto","edward","phil"]
for respondent in respondents:
    if respondent in favorite_languages.keys():
        print("Thanks for your cooperation! "+respondent.title())
    else :
        print("Would you like tell us what's your favorite language? "+respondent.title())

