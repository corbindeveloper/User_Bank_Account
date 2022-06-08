class BankAccount: 
   def __init__(self, int_rate, balance):
      # assign our parameters accordingly
      self.int_rate = int_rate
      self.balance = balance

   def deposit(self, amount):
      self.balance += amount
      return self

   def withdraw(self, amount):
      self.balance -= amount 
      return self

   def display_account_info(self):
      print(f"Balance: {self.balance}")
      return self

   def yield_interest(self):
      if self.balance > 0:
         self.balance = self.balance + (self.int_rate * self.balance)
      return self

account = BankAccount(0.05, 0)
account_two = BankAccount(0.1, 0)

account.deposit(100).deposit(500).deposit(400).withdraw(900).yield_interest().display_account_info()
account_two.deposit(100).deposit(500).withdraw(100).withdraw(100).withdraw(150).withdraw(150).yield_interest().display_account_info()