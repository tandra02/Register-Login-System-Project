# Create a self variable called mapping when initializing (__init__) the system that stores the encryption language
# Create a method called encrypt(self, password) that returns the encrypted password using the mapping dictionary.
# Finally when someone tries to register store the encrypted password instead of the normal one, and when someone tries to log in do the necessary checking.
# To make it happen follow the steps:

# Create a mapping variable that is given in this challenge and save it somewhere in the class so that you could access it via the encrypt method
# Create the encrypt(self, password) method and then use it for the next steps
# When registering a user save his password as an encrypted password in the users dictionary
# When a user tries to log in make sure to encrypt the given input password and check if it matches the saved password in the users dictionary

class LoginSystem:
    def __init__(self):
        self.users = {}
        self.logged_users = set()
        self.mapping = {
            "a" : "i", "b" : "l", "c" : "q", "d" : "f", "e" : "z", "f" : "s",
            "g" : "a", "h" : "g", "i" : "e", "j" : "p", "k" : "w", "l" : "o",
            "m" : "v", "n" : "u", "o" : "b", "p" : "j", "q" : "k", "r" : "n",
            "s" : "x", "t" : "d", "u" : "h", "v" : "y", "w" : "t", "x" : "m",
            "y" : "r", "z" : "c"
        }

    def encrypt(self, password):
        encrypted_password = ''.join([self.mapping[char] for char in password])
        return encrypted_password

    def register(self, username, password):
        if username in self.users:
            print("user already exists")
        else:
            encrypted_password = self.encrypt(password)
            self.users[username] = encrypted_password
            print("user registered successfully")

    def login(self, username, password):
        if username in self.users:
            encrypted_password = self.encrypt(password)
            if encrypted_password == self.users[username]:
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
# Register users
login_system.register('usera', 'passa')
login_system.register('userb', 'passb')
login_system.register('userc', 'passc')

# Attempt to login
login_system.login('usera', 'passa')  # Output: user logged in successfully
login_system.login('userb', 'wrongpass')  # Output: password doesn't match
login_system.login('userd', 'passd')  # Output: user isn't in the system