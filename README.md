# Python Banking Project  

Python project where I implement Python fundamentals that I gained through the SDAxGA bootcamp into one project. The project is about recreating a simple banking application where users can create accounts, withdraw, deposit, and transfer credit from one account to another. It was a good experience that gave me practice working with Python.  

## Technology Used  

- **Python** : the programming language used for the project.  
- **VS Code** : text editor used to write and test the project.  
- **GitHub** : version control and documenting the project.  
- **CSV** : to store the app and customer data.  

## Functionality  
- **Add New Customer**  
    * customer can have a checking account  
    * customer can have a savings account  
    * customer can have both a checking and a savings account  
- **Withdraw Money from Account (required login)**  
    * withdraw from savings  
    * withdraw from checking  
- **Deposit Money into Account (required login)**  
    * can deposit into savings  
    * can deposit into checking  
- **Transfer Money Between Accounts (required login)**  
    * can transfer from savings to checking  
    * can transfer from checking to savings  
    * can transfer from checking or savings to another customer's account  
- **Build Overdraft Protection**  
    * charge customer an overdraft fee of $35 when the account is less than $0.  
    * prevent customer from withdrawing more than $100  
    * _the account cannot have a resulting balance of less than -$100_  
    * deactivate the account after 2 overdrafts  
    * reactivate the account if the customer deposits enough to bring the account balance back to 0.  

## Key Challenges  
- Planning the solution, and having to work with classes and instances.  
- Optimizing some portions of the code so it's efficient and easy to read.  

## IceBox Features  
- Design an interface for the program with HTML and CSS  
