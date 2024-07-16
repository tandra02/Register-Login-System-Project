# Create a method named sign_out(self, username). The method will check if the user exists in the system and then it will check if the user is logged in. If both conditions are met then the method will sign out the user.
# If the user does not exists in the system print: user is not in the system. 
# If the is not logged in print: user is not logged in. 
# If the user signed out successfully print: user signed out successfully

class LoginSystem:
    def __init__(self):
        # Your code here
        self.users = {}
        self.logged_users = set()

    def register(self, username, password):
        if username in self.users:
            print("user already exists")
        else:
            self.users[username] = password
            print("user registered successfully")

    def login(self, username, password):
        if username in self.users: 
            if password == self.users[username]:
                self.logged_users.add(username)
                print("user logged in successfully")
            else:
                print("password doesn't match")
        else:
            print("user isn't in the system")

    def sign_out(self, username):
        if username in self.users:
            if username in self.logged_users:
                self.logged_users.remove(username)
                print("user signed out successfully")
            else:
                print("user is not logged in")
        else:
            print("user is not in the system")



login_system = LoginSystem()
print(login_system.register('usera', 'passa'))
print(login_system.login('usera', 'passa'))