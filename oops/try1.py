class account:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance
    
    def credit(self , amount):
        self.balance += amount
        print("new balance : " , self.check_balance())
    def debit(self, amount):
        if ( amount > self.balance):
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("new balance : " , self.check_balance())
    def check_balance(self):
        return self.balance    
        
    

acc1 =account(13807, 34546000)
acc1.debit(500)
acc1.credit(5000)

   
