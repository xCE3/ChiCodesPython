class User: # here's what we have so far
    def __init__(self, username, email1):
        self.name = username
        self.email = email1
        self.account_balance = 0.00
    # adding the deposit method

    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit
        # the specific user's account increases by the amount of the value received
        self.account_balance += amount
        
    def make_withdrawal(self, amount):  # takes an argument that is the amount of the deposit
        # the specific user's account increases by the amount of the value received
        self.account_balance -= amount


tim = User("Tim Python", "tim@python.com")
fred = User("Fred Python", "fred@python.com")
monty = User("Monty Python", "monty@python.com")

tim.make_deposit(200)
tim.make_deposit(200)
tim.make_deposit(50)
tim.make_withdrawal(5)

monty.make_deposit(50)
monty.make_deposit(50)
monty.make_withdrawal(5)
monty.make_withdrawal(5)

fred.make_deposit(50)
fred.make_withdrawal(5)
fred.make_withdrawal(5)
fred.make_withdrawal(5)
print(tim.account_balance)
print(monty.account_balance)
print(fred.account_balance)
