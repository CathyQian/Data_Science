from threading import Lock
# this above line is critical
class BankAccount(object):
    def __init__(self):
        self.balance = None
        self.lock = Lock()

    def get_balance(self):
        if self.balance is None:
            raise ValueError

        return self.balance

    def open(self):
        with self.lock:
            self.balance = 0

    def deposit(self, amount):
        self._check_amount_and_balance(amount)

        with self.lock:
            self.balance += amount

    def withdraw(self, amount):
        self._check_amount_and_balance(amount)
        if self.balance < amount:
            raise ValueError

        with self.lock:
            self.balance -= amount

    def _check_amount_and_balance(self, amount):
        if amount < 0 or self.balance is None:
            raise ValueError

    def close(self):
        with self.lock:
            self.balance = None
