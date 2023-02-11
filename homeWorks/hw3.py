class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        try:
            money = int(input("введите сумму - "))
            return self._balance + money
        except ValueError:
            return "вводите только числа!"

    def _kill(self):
        kill_balance = self._balance = 0
        return f"ваш баланс - {kill_balance}"

    def __jackpot(self):
        return f"Вы выиграли JACKPOT!!\n" \
               f"ваш баланс - {self._balance * 10}"

    def _stolen_balance(self, other):
        return f"ваш баланс - {self._balance + other._balance}"

ramazan = Bank('roma', 1000)
alim = Bank('alim', 1000)
# print(alim._kill())
print(alim._Bank__jackpot())
print(alim._stolen_balance(ramazan))