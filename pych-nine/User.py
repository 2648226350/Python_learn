class User():
    def __init__(self,given_name,family_name,email):
        self.given_name = given_name
        self.family_name = family_name
        self.email = email
        self.login_attempts = 0
    def describe_user(self):
        print("Name: "+self.given_name.title()+" "+self.family_name.title()+"\nE-mail: "+self.email)
    def greet_user(self):
        print("Hello, "+self.given_name.title()+" "+self.family_name.title()
                +", welcome to use xxxxx.")
    def incre_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

