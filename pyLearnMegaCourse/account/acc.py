class Account:

    def __init__(self,filepath):
        self.filepath = filepath
        with open(filepath,'r') as file:
            self.balance = int(file.read())
    
    def withdraw(self,amount):
        self.balance = self.balance - amount

    def deposit(self,amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as wfile:
            wfile.write(str(self.balance)) 
    
      
class Checking(Account):
    """This sub-class generates checking account objects. This inherits the Base Account class, 
while it has transfer method alone in it."""

    type = "checking"
    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


jack_account = Checking("C:\\Users\\jassm\\Documents\\learn\\tesla\\pyLearnMegaCourse\\account\\jack.txt",10)
print(jack_account.type)
jack_account.transfer(170)
print(jack_account.balance)
jack_account.commit()


john_account = Checking("C:\\Users\\jassm\\Documents\\learn\\tesla\\pyLearnMegaCourse\\account\\john.txt",10)
print("-------")
print(john_account.type)
john_account.transfer(500)
print(john_account.balance)
john_account.commit()

print(john_account.__doc__)