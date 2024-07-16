# User systems requires us to keep track of registered users, and of logged in users.
# Create a class named LoginSystem, that doesn't receive anything in the constructor __init__(self) and initializes a variable users as an empty dictionary and logged_users as an empty set

class LoginSystem:
    def __init__(self):
        self.users = {}
        self.logged_users = set()