import functools
import operator
from money import Money


class Portofolio:
    def __init__(self):
        self.moneys = []
        self._eur_to_usd = 1.2

    def __convert(self, aMoney, aCurrency):
        if aMoney.currency == aCurrency:
            return aMoney.amount

        return aMoney.amount * self._eur_to_usd

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = functools.reduce(
            operator.add, map(lambda m: self.__convert(m, currency), self.moneys)
        )
        return Money(total, currency)