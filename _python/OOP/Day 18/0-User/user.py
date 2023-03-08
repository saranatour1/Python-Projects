class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
      self.account_balance += amount
    def make_withdrawal(self, amount):
      self.account_balance-=amount

    def display_user_balance(self):
      print(f'This is {self.name} and account balance is: {self.account_balance}')
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)

valery=User('valery','valery@gmail.com')
valery.make_deposit(150)
valery.make_deposit(2700)
valery.make_deposit(3000)
valery.make_withdrawal(4000)
valery.display_user_balance()

shadid=User('shadid','shadid@gamail.com')
shadid.make_deposit(1500000)
shadid.make_deposit(1000000)
shadid.make_withdrawal(500000)
shadid.make_withdrawal(5000)
shadid.display_user_balance()

sara=User('sara','sara@gmail.com')
sara.make_deposit(150000)
sara.make_withdrawal(6000)
sara.make_withdrawal(2000)
sara.make_withdrawal(3000)


shadid.transfer_money(sara,16700)
shadid.display_user_balance()
sara.display_user_balance()
# print(1500000+1000000-500000-5000-16700)