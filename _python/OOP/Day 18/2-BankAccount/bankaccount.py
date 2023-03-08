class BankAccount:
	def __init__(self,name, balance ,int_rate=0.05):
		self.name= name
		self.balance=balance
		self.int_rate=int_rate #How do we access this? do we pass it as an argument in the init?
	def deposit(self, amount):
			self.balance+=amount
	def withdraw(self, amount):
			self.balance-=amount
	def display_account_info(self):
			print(f'hello {self.name}, your account balance is {self.balance} ')
	def yield_interest(self):
			 self.balance *= (1 + self.int_rate)

account1=BankAccount('sara',5000)
# account1.display_account_info()

account2=BankAccount('barq',50000)
# account2.display_account_info()

account1.deposit(5000)
account1.deposit(900)
account1.deposit(100)
account1.withdraw(1000)
account1.display_account_info()

account2.deposit(5000)
account2.deposit(900)
account2.withdraw(1000)
account2.withdraw(1000)
account2.withdraw(1000)
account2.withdraw(1000)
account2.yield_interest()
account2.display_account_info()
# print((50000+5000+900-1000*4)*1.05)