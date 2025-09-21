import pprint
import csv
import os

accounts_for_now = {

}

fieldnames = ["id","first_name","last_name","password","checking","savings","active","overdraft_count"]
options = ['1', '2' , '3']

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
def load_accounts():
    try: 
        with open("bank.csv", "r") as file:
            contents = csv.DictReader(file)
            for row in contents:
                cust_id = row['id']
                accounts_for_now[cust_id] = row #will print: {'Name': 'The First Doctor', 'Actor': 'William Hartnell', 'Number of Episodes': '134'}
                # for prop in fieldnames:
                #     print(row[prop]) # will print the value of each individual property
    except csv.Error as e:
        print(e)

def sign_in():
    print()
    print("="*40)
    print("       Sign IN  ")
    print()

    user_id = input('Enter the ID: ')
    print()
    
    while user_id not in accounts_for_now :
        print("Account ID doesn't exists!")
        print()
        user_id = input('Enter the ID: ')
    print()
    print(f"Hi {accounts_for_now[user_id]['first_name']} {accounts_for_now[user_id]['last_name']}")
    print()

    user_pass = input("Enter Password: ")
    print()



    while user_pass != accounts_for_now[user_id]['password'] :
        print("Invalid Password!, Please Try Agin")
        print()
        user_pass = input('Enter Password: ')

    print('Successful! ')
    print()
    pprint.pprint(accounts_for_now[user_id], sort_dicts=False)

        
    

def init():
    load_accounts()
    # pprint.pprint(accounts_for_now, sort_dicts=False)
    print("="*40)
    print("       Welcome to Maher Bank!  ")
    print("="*40)
    print()
    print("1) Sign in")
    print("2) Create account")
    print("3) Quit")
    print()
    print("="*40)

    user_option = input('Pick an option: ')

    while user_option not in options : 
        print('Invalid option')
        user_option = input('Pick an option: ')
    
    if user_option == '1':
        sign_in()


init()