class User:
    def __init__(self, username, email):
        self.name = username
        self.emailAd = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
    	self.account.balance += amount	# hmmm...the User class doesn't have an account_balance attribute anymore
        return self.account.balance

    def make_withdraw(self, amount):
        if amount > self.account.balance:
            return ("INVALID TRANSACTION")
        self.account.balance-= amount
        return self.account.balance

    def display_user_balance(self, amount):
		self.display_user_balance= self.account.balance
        return self.display_user_balance