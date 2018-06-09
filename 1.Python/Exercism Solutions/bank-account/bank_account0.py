class BankAccount(object):
    def __init__(self):
        self.balance = 0
        self.permission = False

    def get_balance(self):
        if self.permission is False:
            raise ValueError("Closed account can't be accessed.")
        return self.balance

    def open(self):
        if self.permission is False:
            self.permission = True

    def deposit(self, amount):
        if self.permission is False:
            raise ValueError("Closed account can't be accessed.")
        elif amount < 0:
            raise ValueError("Can not deposit a negative amount.")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if self.permission is False:
            raise ValueError("Closed account can't be accessed.")
        elif amount < 0:
            raise ValueError("Can not withdraw a negative amount.")
        elif self.balance < amount:
            raise ValueError("Cannot withdraw more than account balance.")
        else:
            self.balance -= amount

    def close(self):
        self.permission = False
