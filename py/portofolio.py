import functools
import operator
from money import Money


class Portofolio:
    def __init__(self):
        self.moneys = []
        self.exchange_rates = {
            "EUR->USD": 1.2,
            "EUR->KRW": 1344,
            "USD->EUR": 0.82,
            "USD->KRW": 1100,
            "KRW->USD": 0.00090,
            "KRW->EUR": 0.00073,
        }

    def __convert(self, aMoney, aCurrency):
        if aMoney.currency == aCurrency:
            return aMoney.amount

        return aMoney.amount * self.exchange_rates[f"{aMoney.currency}->{aCurrency}"]

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = 0.0
        failures = []
        for m in self.moneys:
            try:
                total += self.__convert(m, currency)
            except KeyError as ke:
                failures.append(ke)

        if len(failures) == 0:
            return Money(total, currency)
        
        failureMessage = ",".join(f.args[0] for f in failures)
        raise Exception("Missing exchange rate(s):[" + failureMessage + "]")