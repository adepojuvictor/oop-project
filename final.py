## creating a full banking system
class Account:
    def __init__(self, acct_name, acct_number, acct_balance):
        self.acct_name = acct_name
        self.acct_number = acct_number
        self.__acct_balance = acct_balance

    def set_balance(self, new_balance):
        self.__acct_balance = new_balance
    
    def get_acct_number(self):
        return self.acct_number
    

    def get_balance(self):
        return self.__acct_balance

    def deposit_money(self, amount) :
        self.__acct_balance += amount
        print(f"{self.acct_name} deposited {amount}. current balance : {self.__acct_balance}")
    
    def withdraw(self, amount) :
        if self.__acct_balance >= amount :
            self.__acct_balance -= amount
            print(f"{self.acct_name} withdrew {amount}. Your current balance is {self.__acct_balance} ")
        else :
            print("i'm sorry, you don't have enough balance in your account")

    def __str__(self):
        return f"{self.acct_name} - {self.acct_number} - {self.__acct_balance}"
    

class savings_account(Account) :
    def __init__(self, acct_name, acct_number, acct_balance, interest_rate):
        super().__init__(acct_name, acct_number, acct_balance)
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        interest = self.__acct_balance * self.interest_rate
        self.deposit(interest)

    def deposit_money(self, amount):
        interest = amount * (self.interest_rate/100)
        total_amount = amount + interest
        self.__acct_balance += total_amount
        print(f"{self.acct_name} deposited {amount} - current balance {self.__acct_balance}")
    
    
class Bank :
    def __init__(self, bank_name, bank_address, bank_colour):
        self.bank_name = bank_name
        self.bank_address = bank_address
        self.bank_colour = bank_colour
        self.customer = []

    def latest_customers(self, name, acct_number, address) :
        latest_customer_detail = Account(name, acct_number, address,)
        self.customer.append(latest_customer_detail)
        return latest_customer_detail
    
    def __str__(self):
        return f"{self.bank_name} - {self.bank_address} - {self.bank_colour} - {len(self.customer)}"
    

        

        

acct1 = Account("victor", 112233445566, 600000)
acct1.deposit_money(2000)
acct1.withdraw(10000)
acct1.set_balance(700)
print(acct1.get_balance())
acct1.deposit_money(500000)
print(acct1)

bank = Bank("victor bank", "Akure,Ondo","white" )
bank.latest_customers("victor.AD", "09152798547", "Oyo")
print(bank)

savings = savings_account("segun", "9152798547", 25000, 1.5 )
savings.calculate_interest()
print(savings)





        
        