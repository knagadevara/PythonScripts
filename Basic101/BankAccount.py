#!/usr/bin/python3.6

class BankAccount:

    stock_cash = 10000

    def __init__(self, fname, lname, dob, uaccount):
        self.first = fname
        self.last  = lname
        self.bday = dob
        self.accid = uaccount
        self.balance = 0.0

    def deposit(self, damount):
        #self.updateamount = self.damount
        BankAccount.stock_cash += damount
        self.balance += damount
    
    def withdrawl(self, wamount):
        if self.balance >= wamount:

            BankAccount.stock_cash -= wamount
            self.balance -= wamount
        else:
            print('Hi, {0} you have low Balance cannot process a Withdrawl.'.format(self.first))

    def details(self):
        print("{0}, {1}.".format(self.first[0], self.last))
        print("Account No.: {0}".format(self.accid))
        print("Account Balance: {0}".format(self.balance))

    
u1 = BankAccount('Karthik', 'Nagadevara', 1991 , 9700556677)
u2 = BankAccount('Murgan' , 'Aravedagan', 1992 , 9666166127)
u3 = BankAccount('Bharath' , 'Basuth' , 1992 , 9623241)
#u1.details()
u1.deposit(9853)
u2.withdrawl(500)
u1.details()
u2.details()
u3.details()
