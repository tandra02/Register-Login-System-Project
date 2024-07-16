# Create a method called login(self, username, password) that checks if the users exists in the system, and if it is then it will check if the password matches the password that is stored in the system. if both conditions are met then store the username in the logged_users variable.
# If the user logged in print: user logged in successfully. 
# If the user is not in the system print: user isn't in the system. 
# If the password doesn't match print: password doesn't match

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



login_system = LoginSystem()

# Register users
login_system.register('usera', 'passa')
login_system.register('userb', 'passb')
login_system.register('userc', 'passc')

# Attempt to login
login_system.login('usera', 'passa')  # Output: user logged in successfully
login_system.login('userb', 'wrongpass')  # Output: password doesn't match
login_system.login('userd', 'passd')  # Output: user isn't in the system