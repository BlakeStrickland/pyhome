import re

class Currency:

    def __init__(self, amount, currency_code=None):
        codes = {
        "$": "1.0",
        "E": "0.87859",
        "Ω": "0.5"
        }
        self.amount = amount
        self.currency_code = currency_code


        if type(self.amount) is str:
            self.amount = amount.strip()

        if self.currency_code == None:
            self.currency_code = amount[0]
            self.amount = amount[1:]
        else:
            self.currency_code = currency_code
            self.amount = amount

    def __eq__(self, other):
        return self.currency_code == other.currency_code and self.amount == other.amount

    def __add__(self, other):
        if self.currency_code == other.currency_code:
            return Currency((self.amount + other.amount), self.currency_code)
        else:
            return False

    def __sub__(self, other):
        if self.currency_code == other.currency_code:
            return self.amount - other.amount
        else:
            raise Exception("Cant subtract two different currency types")

    def __mul__(self, other):
        if self.currency_code == other.currency_code:
            try:
                int(self.amount) and int(other.amount)
                return self.amount * other.amount
            except:
                print("haxorz")
        else:
            raise Exception("well i tried")

money1 = Currency("$100")
money2 = Currency(500, "$")

print(money1.amount)
print(money1.currency_code)
print(money2.amount)
print(money2.currency_code)
