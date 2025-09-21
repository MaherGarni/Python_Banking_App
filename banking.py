import pprint
import csv
import os

fieldnames = ["id","first_name","last_name","password","checking","savings","active","overdraft_count"]
options = ['1', '2' , '3']


class User:
    def __init__(self , id,first_name, last_name, password , accounts = [None ,None], active = True , overdraft_count=0):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.accounts = accounts 
        self.active = active
        self.overdraft_count = overdraft_count     


    def __str__(self):
        return f"{self.id} , {self.first_name} {self.last_name} , {self.password} , {self.accounts} , {self.active} , {self.overdraft_count}"
    
class Account:
    def __init__(self, owner,balance = 0):
        self.owner = owner
        self.balance = balance
class Checking(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

class Savings(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

class Bank:
    def __init__(self):
        self.users = {}
        self.ids= 100013
        self.load_users()


    def prepare_user(self, **Kkwargs):
        info = Kkwargs
        user = User(info['id'] , info['first_name'], info['last_name'], info['password'] , [info['checking'] , info ['savings']] , info['active'] , info ['overdraft_count']) 
        return user

    
    def load_users(self):
        try: 
            with open("bank.csv", "r") as file:
                contents = csv.DictReader(file)
                for row in contents:
                    user = self.prepare_user(**row)
                    self.users[user.id] = user 
        except csv.Error as e:
            print(e)

    def sign_in(self):
        print()
        print("="*40)
        print("       Sign IN  ")
        print()

        user_id = input('Enter the ID: ')
        print()

        while user_id not in self.users :
            print("Account ID doesn't exists!")
            print()
            user_id = input('Enter the ID: ')
        print()
        print(f"Hi {self.users[user_id]['first_name']} {self.users[user_id]['last_name']}")
        print()

        user_pass = input("Enter Password: ")
        print()



        while user_pass != self.users[user_id]['password'] :
            print("Invalid Password!, Please Try Agin")
            print()
            user_pass = input('Enter Password: ')

        print('Successful! ')
        print()
        pprint.pprint(self.users[user_id], sort_dicts=False)
    
    def create_user(self):
        print()
        print("="*40)
        print("       Create User  ")
        print()
        user_first_name = input('Enter First Name: ')
        print()
        user_last_name = input('Enter Last Name: ')
        print()
        user_password = input('Enter Password: ')
        print()

        user = User(self.ids , user_first_name, user_last_name,user_password)
        self.users[user.id] = user
        self.ids +=1
        print('User is created successfully')
        for idx , user in self.users.items():
            print(user)
        print(self.ids)


        # write to csv 


        


# 3.0 Check CSV File Exists (otherwise error thrown!)
# 3.1 Set Headers in the CSVFile 
# 3.2 SEED DATA TO CSV
# 3.3 EXAMPLE: writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
# 3.4 "w" option will allow writing, but NOT appending...
# if not os.path.exists("./doctor_who.csv"):
#     with open("./doctor_who.csv", 'w', newline='') as csvfile:
#         try:
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#             writer.writeheader()
#             for row in doctor_who_info:
#                 writer.writerow(row)
#         except csv.Error as e:
#             print(e)


# 4.0 If Exists - ReadFile / Rows:


# def sign_in():
#     print()
#     print("="*40)
#     print("       Sign IN  ")
#     print()

#     user_id = input('Enter the ID: ')
#     print()
    
#     while user_id not in accounts_for_now :
#         print("Account ID doesn't exists!")
#         print()
#         user_id = input('Enter the ID: ')
#     print()
#     print(f"Hi {accounts_for_now[user_id]['first_name']} {accounts_for_now[user_id]['last_name']}")
#     print()

#     user_pass = input("Enter Password: ")
#     print()



#     while user_pass != accounts_for_now[user_id]['password'] :
#         print("Invalid Password!, Please Try Agin")
#         print()
#         user_pass = input('Enter Password: ')

#     print('Successful! ')
#     print()
#     pprint.pprint(accounts_for_now[user_id], sort_dicts=False)

# def create_account():
#     print()
#     print("="*40)
#     print("       Sign IN  ")
#     print()

#     # user_id = input('Enter the ID: ')
#     # for idx ,user in self.users.items():

        
    

def init():
    bank = Bank()

    for idx ,user in bank.users.items():
        print(user)
    print("="*40)
    print("       Welcome to Maher Bank!  ")
    print("="*40)
    print()
    print("1) Sign in")
    print("2) Create User")
    print("3) Quit")
    print()
    print("="*40)

    user_option = input('Pick an option: ')

    while user_option not in options : 
        print('Invalid option')
        user_option = input('Pick an option: ')
    
    if user_option == '1':
        bank.sign_in()
    if user_option == '2':
        bank.create_user()


init()