import pprint
import csv
import os

fieldnames = ["id","first_name","last_name","password","checking","savings","active","overdraft_count"]
options = ['1','2','3','4','5']

class User:

    def __init__(self, id, first_name, last_name, password , checking="False", savings="False", active = True , overdraft_count=0):
        self.id = id
        self.first_name = first_name
        self.last_name  = last_name
        self.password   = password
        self.checking   = False if checking == "False" or checking == False else int(checking)
        self.savings    = False if savings == "False" or savings == False else int(savings)
        self.active     = False if active == "False" else True
        self.overdraft_count = overdraft_count     

    # def get
    def __str__(self):
        return f"{self.id} , {self.first_name} {self.last_name} , {self.password} , {self.checking}, {self.savings} , {self.active} , {self.overdraft_count}"
    

class Bank:

    def __init__(self):
        self.users = {}
        self.load_users()
        self.ids =  100000 + len(self.users) + 1
        self.user = None
    
    def load_users(self):
        try: 
            with open("bank.csv", "r") as file:
                contents = csv.DictReader(file)
                for row in contents:
                    self.users[row["id"]] = User(row['id'] , row['first_name'], row['last_name'], row['password'] , row['checking'] , row ['savings'], row['active'] , row ['overdraft_count'])  
        except csv.Error as e:
            print(e)

    def sign_in(self):
        print()
        print("="*40)
        print("       Sign IN  \n\n")

        user_id = None
        while not user_id or user_id not in self.users:
            user_id = input('Enter the ID: \n')
            if user_id not in self.users:
                print("Account ID doesn't exists! \n")
        
        print(f"Hi {self.users[user_id].first_name} {self.users[user_id].last_name} \n")

        user_pass = None
        while not user_pass or user_pass != self.users[user_id].password:
            user_pass = input('Enter Password: ')
            if user_pass != self.users[user_id].password:
                print("Invalid Password!, Please Try Agin. \n\n")

        print('Successful! \n')
        self.user = self.users[user_id]

    
    def create_user(self):

        print("="*40)
        print("       Create User  \n")
        user_first_name = input('Enter First Name: ')
        print()
        user_last_name  = input('Enter Last Name: ')
        print()
        user_password   = input('Enter Password: ')
        print()
        user = User(self.ids , user_first_name, user_last_name,user_password)
        self.users[user.id] = user
        self.ids +=1
        self.user = user
        
        try:
            new_row = { 'id': user.id,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'password' : f'{user.password}',
                        'checking': user.checking,
                        'savings' : user.savings,
                        'active' : user.active,
                        'overdraft_count' : user.overdraft_count}
            
            with open("bank.csv", "a+") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(new_row)
        except csv.Error as e:
            print(e)

        print('User Created Successfully')


    def user_menu (self):

        print("="*40)
        print(f"       Hi {self.user.first_name} {self.user.last_name}!  ")
        print("="*40)
        print("\n1) Create Account")
        print("2) Withdraw")
        print("3) Deposit")
        print("4) Tansfer")
        print("5) Log Out\n")
        print("="*40)

        user_option = None
        while not user_option or user_option not in options:
            user_option = input("Pick an option: ")
            if user_option not in options:
                print('Invalid Option, try again')

        match user_option:
            case '1':
                self.create_account()
            case '2':
                self.withdraw()
            case '3':
                pass
            case '4':
                pass
            case '5':
                return False
        return True

    def create_account(self):
        if type(self.user.checking) != bool and type(self.user.savings) != bool:
            print("U have checking and savings accounts already, you can't create more \n" )
            return
        
        print(f"\n       Pick checking or savings   ")
        print("="*40)
        print("1) Checking")
        print("2) Savings")
        print("="*40)

        user_option = None
        while not user_option or user_option not in options[:2]:
            user_option = input("Pick an option: ")
            if user_option not in options[:2]:
                print('Invalid Option, try again')
        
        if user_option == '1':
            if type(self.user.checking) == bool:
                self.user.checking = 0
                print("Checking account created successfully") 
            else:
                print ("you already have checking account")
        if user_option == '2':
            if type(self.user.savings) == bool:
                self.user.savings = 0
                print("Savings account created successfully") 
            else:
                print ("you already have savings account")
        
        self.update_csv()

    def withdraw(self):

        if not self.user.active :
            print('Sorry, your account is deactivated!\nYou need to have positive balance to activate your account')
            return
        if type(self.user.checking) == bool and type(self.user.savings) == bool :
            print('Sorry, you need to create account first')
            return
        
        print(f"\n       Withdraw from checking or savings   ")
        print("="*40)
        print("1) Checking")
        print("2) Savings")
        print("="*40)

        user_option = None
        while not user_option or user_option not in options[:2]:
            user_option = input("Pick an option: ")
            if user_option not in options[:2]:
                print('Invalid Option, try again')
        
        if user_option == '1':
            if type(self.user.checking) == bool:
                print("You don't have checking account")
                return
        if user_option == '2':
            if type(self.user.savings) == bool:
                print("You don't have savings account")
                return
        
        user_amount = None
        while not user_amount or type(user_amount) != int:
            user_amount = input('Enter the amount to withdraw: ')
            if user_amount.strip().isnumeric():
                user_amount = int(user_amount)
                if user_amount > 100 :
                    print("Sorry, you can't withdraw more than 100 in one transaction")
                    user_amount = None
            else:
                print('Invalid, please enter valid number')

        if user_option == '1':
            self.user.checking -= user_amount
            print(f'Success, your current balance: {self.user.checking}')
        else:
            self.user.savings -= user_amount
            print(f'Success, your current balance: {self.user.savings}')
            
        
        self.update_csv()

        # overdraf ?
        # fee ?
    
    def update_csv(self):
        if os.path.exists("bank.csv"):
            with open("bank.csv", 'w', newline='') as csvfile:
                try:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    for row in self.users.values():
                        writer.writerow(row.__dict__)
                except csv.Error as e:
                    print(e)
        self.load_users()



def init():

    bank = Bank()

    print("="*40)
    print("       Welcome to Maher Bank!  ")
    print("="*40)
    print("1) Sign in")
    print("2) Create User")
    print("3) Quit")
    print()
    print("="*40)

    user_option = input('Pick an option: ')

    while user_option not in options:
        print('Invalid option')
        user_option = input('Pick an option: ')
    
    if user_option == '1':
        bank.sign_in()
    if user_option == '2':
        bank.create_user()

    if bank.user:
        bank.user_menu()



init()