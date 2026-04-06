class Account():
    # Balance And pin
    
    def __init__(self,Balance,pin):
        self.Balance=Balance
        self.pin=pin
        self.login_=False
        self.History=[]
    # Check the Login Pin
    
    def Login_Account(self,login_pin):
        self.login_pin=login_pin
        if login_pin==self.pin:
            print("Login Successful")
            self.login_=True
        else:
            print("Login Unsuccessful")
    # Check debit amount
    
    def debit(self,amount):
        if self.login_:
            self.Balance-=amount
            print("RS.",amount,"is debited")
            print("The Balance is:",self.get_balance())
            self.History.append(f"Debited:{amount}")
        else:
            print("Login First")
    # Check Credit amount
    
    def credit(self,amo):
        if self.login_:
            self.Balance+=amo
            print("RS.",amo,"is credited")
            print("The balance is:",self.get_balance())
            self.History.append(f"Credited:{amo}")
        else:
            print("Please Login first")
    # View the Account Balance
    
    def get_balance(self):
        return self.Balance
    
    def history(self):
        return self.History
# Print the values

A1=Account(5000,9525)
while True:
    A1.Login_Account(int(input("Enter the pin:")))
    A1.debit(250)
    A1.credit(500)
    print(A1.History)