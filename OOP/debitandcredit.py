class Account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no


    def debit(self,ammount):
        self.balance-=ammount
        print("Rs.",ammount,"was debited!")
        print("Total balance=",self.get_balance())

    def credit(self,ammount):
            self.balance+=ammount
            print("Rs.",ammount,"was credited!")
            print("Total balance=",self.get_balance())


    def get_balance(self):
         return self.balance



acc1=Account(1000,"12Ac")

acc1.debit(100)
acc1.credit(200)
