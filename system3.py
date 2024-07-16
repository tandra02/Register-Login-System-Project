# To allow users to register create a method register(self, username, password) that receives username and password. 
# All of our registered users will be stored inside the variable users that we initialized in the previous lesson. The keys are the usernames and the values are the passwords. The method will check if a user is already registered in the system, if he isn't in the system register him and print user registered successfully. If the user already registered print: user already exists

class LoginSystem:
    def __init__(self):
        self.users = {}
        self.logged_users = set()

    def register(self, username, password):
        if username in self.users:
            print("user already exists")
        else:
            self.users[username] = password
            print("user registered successfully")


login_system = LoginSystem()

# Register users
login_system.register([('usera', 'passa'), ('userb', 'passb'), ('userc', 'passc'), ('userc', 'passc'), ('userd', 'passd')]
[('usera', 'usera'), ('usera', 'passa'), ('usera', 'passa')])
login_system.register("user1", "password1")  # Output: user registered successfully
login_system.register("user2", "password2")  # Output: user registered successfully
login_system.register("user1", "password3")  # Output: user already exists