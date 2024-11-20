class Account:
    def __init__(self, full_name, acc_number, balance, phone):#constructor used to set up info
        #self means the actual object or the  object itself
        self.full_name = full_name
        self.acc_number = acc_number
        self.balance = balance
        self.phone = phone
    def deposit(self,amount):
        self.balance  +=  amount
        print(f'amount {amount} has been deposited to {self.acc_number}')

    def withdraw(self,amount):
         if self.balance < amount:
             print(f'{self.full_name} has not enough balance and balance is {self.balance}')

         else:
             self.balance -= amount
             print(f'{self.full_name} has been withdrawn from {self.acc_number}')

    def check_balance(self):
        print(f'balance for account {self.full_name} is {self.balance}')

#data and methods that manipulate data
#bject
sam_acc= Account(full_name='samwel maina', acc_number='17708', balance=1000, phone='0715733966')# calling my objects
david_acc=Account(full_name='david maina',acc_number='19968',balance=8000,phone='0715710889')
sam_acc.deposit(2000)
sam_acc.check_balance()
sam_acc.withdraw(10)
sam_acc.check_balance()
david_acc.deposit(1000)
david_acc.check_balance()
