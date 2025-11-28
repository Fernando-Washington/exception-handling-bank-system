from datetime import datetime
from exceptions import NegativeValueError, InvalidValueError

class Transaction:
    def __init__(self, type: str, value: float, account):
        self._type = type
        self._value = value
        self._account = account
        self._date = datetime.now()


class Account:
    def __init__(self, number, client, balance, password):
        self._number = number
        self._client = client
        self._balance = balance
        self._password = password

    def deposit(self, value):
        if value <= 0:
            raise NegativeValueError(value)

        self._balance += value
        print(f"Depósito realizado. Novo saldo: {self._balance}")

    def withdraw(self, value):
        if value <= 0:
            raise NegativeValueError(value)

        if value > self._balance:
            raise InvalidValueError("Saldo insuficiente.")

        self._balance -= value
        print(f"Saque realizado. Saldo atual: {self._balance}")


class Current_account(Account):
    def __init__(self, number, client, balance, password, limit):
        super().__init__(number, client, balance, password)
        self._limit = limit

    def withdraw(self, value):
        if value <= 0:
            raise NegativeValueError(value)

        if value > (self._balance + self._limit):
            raise InvalidValueError("Limite insuficiente.")

        self._balance -= value
        print(f"Saque realizado. Saldo atual: {self._balance}")
