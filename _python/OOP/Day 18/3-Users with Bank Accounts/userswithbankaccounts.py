class User:
  def __init__(self, name, email, accounts):
    self.name = name
    self.email = email
    self.accounts = accounts
  
  def make_deposit(self, amount, account_num):
    self.accounts[account_num].deposit(amount)
  def make_withdrawal(self, amount, account_num):
    self.accounts[account_num].withdraw(amount)
  def display_balance(self, account_num):
    return self.accounts[account_num].display_account_info()

    
class BankAccount:
    def __init__(self, balance ,int_rate):
      self.balance=balance
      self.int_rate=int_rate #How do we access this? do we pass it as an argument in the init?
    def deposit(self, amount):
      self.balance+=amount
      return self
    def withdraw(self, amount):
      self.balance-=amount
    def display_account_info(self):
      return self.balance
    def yield_interest(self):
      self.balance *= (1 + self.int_rate)


account1 = BankAccount(100, 0.05)
account2 = BankAccount(200, 0.1)
user1 = User('Sara', 'sara@gmail.com', [account1, account2])
user1.make_deposit(50, 0)  
user1.make_deposit(100, 1)  
user1.make_withdrawal(500, 1)  
print(user1.display_balance(0))  
print(user1.display_balance(1))  

