from User import User
class Privileges():
    def __init__(self,privileges = ['can add post','can delete post','can ban user']):
        self.privileges = privileges
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege.title().ljust(30),end = "")
        print()
class Admin(User):
    def __init__(self,given_name,family_name,email):
        super(Admin,self).__init__(given_name,family_name,email)
        self.privileges = Privileges()