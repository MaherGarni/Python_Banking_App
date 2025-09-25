import pprint
import csv
import os

fieldnames = ["id","first_name","last_name","password","checking","savings","active","overdraft_count"]
options = ['1','2','3','4','5']

def print_to_screen(header, options):
    print("\n\t", header)
    print("="*40)
    for option in options:
        print(option)
    print("="*40)


class User:

    def __init__(self, id, first_name, last_name, password , checking="False", savings="False", active = True , overdraft_count=0):
        self.id = id
        self.first_name = first_name
        self.last_name  = last_name
        self.password   = password
        self.checking   = False if checking == "False" or checking == False else int(checking)
        self.savings    = False if savings == "False" or savings == False else int(savings)
        self.active     = False if active == "False" else True
        self.overdraft_count = int(overdraft_count)     

    def __str__(self):
        return f"{self.id} , {self.first_name} {self.last_name} , {self.password} , {self.checking}, {self.savings} , {self.active} , {self.overdraft_count}"
    

class Bank:

    def __init__(self):
        self.users = {}
        self.load_users()
        self.ids =  100000 + len(self.users) + 1
        self.user = None # 
        self.acct_choice = 'checking'
    
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
        print(f"       account accessed: { self.acct_choice}  ")
        print("="*40)


# does the user have checking, savings, or both?
# if checking Falseand Savings False:
# pleasse choose an acount tyypeto create


# if checking and not savings
    # offer menu..
    # 1 - create savings
    # 2 - ...
# if savings and not checking
    # offer menu..
    # 1 - create checking
    # 2 - 
       
       
        # account_choice = None
        
        # if self.user.active and self.user.checking and self.user.savings:2
        # print("\n1) Create Account ")
        # print("which acount would you like to access")
        # print("2) Withdraw")
        # print("3) Deposit")
        # print("4) Tansfer")
        # print("5) Log Out\n")
        # print("="*40)

            
        # if self.user.active and self.user.checking:
        #     print("these are your options withdraw, deposit, transfer")
        #     print("2) Withdraw")
        # print("3) Deposit")
        # print("4) Tansfer")
        # print("5) Log Out\n")
        # print("="*40)


        # if self.user.active and self.user.savings:
        #     print("these are your options withdraw, deposit, transfer")
        #     print("2) Withdraw")
        # print("3) Deposit")
        # print("4) Tansfer")
        # print("5) Log Out\n")
        # print("="*40)


        


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
                self.deposite()
            case '4':
                self.transfer()
                pass
            case '5':
                return False
        return True

    def create_account(self):
        
        if type(self.user.checking) == bool and type(self.user.savings):

            print(f"\n       Create Accont   ")
            print("="*40)
            print("1) Checking")
            print("2) Savings")
            print("3) Both")
            print("="*40)

            user_option = None
            while not user_option or user_option not in options[:4]:
                user_option = input("Pick an option: ")
                if user_option not in options[:4]:
                    print('Invalid Option, try again')

            if user_option == '1':
                self.user.checking = 0
                print("Checking account created successfully") 
            if user_option == '2':
                self.user.savings = 0
                print("Savings account created successfully") 
            if user_option == '3':
                self.user.checking = 0
                self.user.savings = 0
                print("Accounts created successfully")
       
        self.update_csv()

    def account_access(self):

        if type(self.user.checking) != bool and  type(self.user.savings) != bool :
            print_to_screen('Which account to access' , ['1) Checking' , '2) Savings'])
            user_option = None
            while not user_option or user_option not in options[:3]:
                user_option = input("Pick an option: ")
                if user_option not in options[:3]:
                    print('Invalid Option, try again')
            if user_option == '1':
                self.acct_choice = 'checking'
            if user_option == '2':
                self.acct_choice = 'savings'

        if type(self.user.checking) != bool and type(self.user.savings) == bool:
            print_to_screen('Pick Option' , ['1) Chickeng' , '2) Create savings account'])
            user_option = None
            while not user_option or user_option not in options[:3]:
                user_option = input("Pick an option: ")
                if user_option not in options[:3]:
                    print('Invalid Option, try again')
            if user_option == '1':
                self.acct_choice = 'checking'
            if user_option == '2':
                self.user.savings = 0
                self.acct_choice = 'savings'

        if type(self.user.checking) == bool and type(self.user.savings) != bool:
            print_to_screen('Pick Option', ['1) Savings' , '2) Create checking account'])
            user_option = None
            while not user_option or user_option not in options[:3]:
                user_option = input("Pick an option: ")
                if user_option not in options[:3]:
                    print('Invalid Option, try again')
            if user_option == '1':
                self.acct_choice = 'savings'
            if user_option == '2':
                self.user.checking = 0
                self.acct_choice = 'checking'

        self.update_csv()

    def withdraw(self):
        print(f"\n       Withdraw    ")
        print("="*40)

        user_amount = self.user_amount('w')

        curr_balance = getattr(self.user, self.acct_choice)
        if curr_balance > 0 and user_amount < curr_balance:
            new_balance = curr_balance - user_amount
            setattr(self.user , self.acct_choice,new_balance)
            print(f'Success, your current {self.acct_choice} balance: {new_balance}')
        else:
            self.over_draft_calc(user_amount, curr_balance)
            

        self.update_csv()

    def over_draft_calc(self , amount, curr_balance):
        if  curr_balance - amount < -65 :
            print(f'Sorry, not allowed, account balance can not go below -100')
            return
        
        curr_balance -= amount + 35
        setattr(self.user , self.acct_choice , curr_balance)
        print(f'Success, your current {self.acct_choice} balance: {curr_balance}, note that an overdraft fee is added')
        self.user.overdraft_count += 1
        if self.user.overdraft_count == 2:
             self.user.active = False
             print('your account is now deactivated, need to deposite to activate it')

    def user_amount(self , op):
        user_amount = None
        if op == 'w':
            print('w')
            while not user_amount or type(user_amount) != int:
                user_amount = input('Enter the amount to withdraw: ')
                if user_amount.strip().isnumeric():
                    user_amount = int(user_amount)
                    if user_amount > 100 :
                        print("Sorry, you can't withdraw more than 100 in one transaction")
                        user_amount = None
                else:
                    print('Invalid, please enter valid number')
        else:
            while not user_amount or type(user_amount) != int:
                user_amount = input(f'Enter the amount to {op}: ')
                if user_amount.strip().isnumeric():
                    user_amount = int(user_amount)
                else:
                    print('Invalid, please enter valid number')

        return user_amount
    
    def deposite(self):
        print(f"\n       Deposite    ")
        print("="*40)

        user_amount = self.user_amount('deposite')

        curr_balance = getattr(self.user , self.acct_choice)
        new_balance = curr_balance + user_amount
        setattr(self.user , self.acct_choice , new_balance)
        print(f'Success, your current {self.acct_choice} balance: {new_balance}')
        if curr_balance < 0 and new_balance >= 0 :
            self.user.overdraft_count = 0
            if not self.user.active:
                print('Your account is now activated')
                self.user.active = True


        self.update_csv()
    
    def transfer(self):
        other_acct = 'savings' if self.acct_choice == 'checking' else 'checking'
        print_to_screen('Transfer' , [f'1) transfer to {other_acct}' , '2) transfer to another user'])

        user_option = None
        while not user_option or user_option not in options[:3]:
            user_option = input("Pick an option: ")
            if user_option not in options[:3]:
                print('Invalid Option, try again')
        
        if user_option == '1' :
            amount = self.user_amount('transfer')
            curr_acct_balance = getattr(self.user , self.acct_choice) - amount
            setattr(self.user , self.acct_choice , curr_acct_balance)
            other_acct_balance = getattr(self.user , other_acct) + amount
            setattr(self.user , other_acct , other_acct_balance)
            print(f'Succsess, your {self.acct_choice} balance: {curr_acct_balance}, and your {other_acct} is now : {other_acct_balance}   ')
            


        self.update_csv()

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



def init():

    bank = Bank()

    print_to_screen(" Welcome to Maher Bank!", ["1) Sign in", "2) Create User", "3) Quit"])

    user_option = input('Pick an option: ')
    while user_option not in options:
        print('Invalid option')
        user_option = input('Pick an option: ')
    
    if user_option == '1':
        bank.sign_in()

    if user_option == '2':
        bank.create_user()
        bank.create_account()

    if bank.user:
        bank.account_access()
        bank.user_menu()



init()