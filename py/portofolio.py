import functools
import operator
from money import Money


class Portofolio:
    def __init__(self):
        self.moneys = []
        self.exchange_rates = {
            "EUR": {
                "USD": 1.2,
                "KRW": 1344,
            },
            "USD": {
                "EUR": 0.82,
                "KRW": 1100,
            },
            "KRW": {
                "USD": 0.00090,
                "EUR": 0.00073,
            },
        }

    def __convert(self, aMoney, aCurrency):
        if aMoney.currency == aCurrency:
            return aMoney.amount

        return aMoney.amount * self.exchange_rates[aMoney.currency][aCurrency]

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = functools.reduce(
            operator.add, map(lambda m: self.__convert(m, currency), self.moneys)
        )
        return Money(total, currency)