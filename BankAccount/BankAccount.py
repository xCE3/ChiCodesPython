# Creating BankAccount class
class BankAccount:
	# don't forget to add some default values for these parameters!
	def __init__(self, int_rate, bal):
        self.interest_rate = int_rate
        self.balance = bal  # don't worry about user info here; we'll involve the User class soon

# Method to show balance after depositing cash to bank account
    def deposit(self,amount):
        self.balance+= amount
        return self.balance

# Method that updates balance after withdrawal,no transation if amount>balance
    def withdraw(self, amount):
        if amount > self.balance:
            return ("INVALID TRANSACTION")
        self.balance-= amount
        return self.balance


	def display_account_info(self):
		self.display_account_info = self.int_rate, self.balance
        return self.display_account_info

	def yield_interest(self):
        if amount > 0
            return amount * self.int_rate
		self.yield_interest = amount
        return self.yield_interest

tim = Account("Tim Python", "tim@python.com")
monty = Account("Monty Python", "monty@python.com")

tim.make_deposit(200).make_deposit(200).make_deposit(50).make_withdrawal(5).yield_interest.display_account_info
montyAccount.deposit(40000)tim.make_deposit(200).make_withdrawal(200).make_withdrawal(50).make_withdrawal(5).make_withdrawal(200).yield_interest.display_account_info
