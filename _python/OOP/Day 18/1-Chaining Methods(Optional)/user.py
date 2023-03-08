class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
      self.account_balance += amount
      return self
 
    def make_withdrawal(self, amount):
      self.account_balance-=amount
      return self

    def display_user_balance(self):
      print(f'This is {self.name} and account balance is: {self.account_balance}')
      return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

valery=User('valery','valery@gmail.com')
valery.make_deposit(150).make_deposit(2700).make_deposit(3000).make_withdrawal(4000).display_user_balance()

shadid=User('shadid','shadid@gamail.com')
shadid.make_deposit(1500000).make_deposit(1000000).make_withdrawal(500000).make_withdrawal(5000).display_user_balance()

sara=User('sara','sara@gmail.com').make_deposit(150000).make_withdrawal(6000).make_withdrawal(2000).make_withdrawal(3000).transfer_money(shadid,16700).display_user_balance()


# print(1500000+1000000-500000-5000-16700)