import json
import os 

class User():
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository():
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('user.json'):
            with open('users.json','r',encoding='utf-8') as file:
                users =  json.load(file)
                
                for user in users : 
                    user = json.loads(user)
                    newUser = User(username = user['username'], password= user['password'],email= user['email'])
                    self.users.append(newUser)
            print(self.users)

    def logout(self):
        self.isLoggedIn = False 
        self.currentUser = {}
        print("Logout success.")
            
    def identity(self):
       if self.isLoggedIn :
           print(f'Username :  {self.currentUser.username}')
       else : 
            print("Not logged in ")
        
    
    def register(self, user: User):
        self.users.append(user)
        self.saveToFile()
        print("User created.")

    def login(self,username,password):
        for user in self.users:
            if user.username == username and user.password == password : 
                self.isLoggedIn = True
                self.currentUser = user
                print('Login success.')
                break


    def saveToFile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open('users.json', 'w') as file:
            json.dump(list, file)


repository = UserRepository()


while True:
    print('Menu'.center(50, '*'))
    choice = input(
        '1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\n Your choice : ')
    if choice == '5':
        break
    else:
        if choice == '1':
            username = input('Username : ')
            password = input('Password : ')
            email = input('Email : ')

            user = User(username, password, email)
            repository.register(user)

        elif choice == '2':
            if repository.isLoggedIn:
                print("Your already logged in . ")
            else: 
                username = input('Username : ')
                password = input('Password : ')
                repository.login(username,password)
            
        
        elif choice == '3':
            repository.logout()
        elif choice == '4':
           repository.identity()
        else:
            print("Wrong choice")
