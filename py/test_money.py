import unittest
from money import Money
from portofolio import Portofolio


class TestMoney(unittest.TestCase):
    def testMultiplicationInDollars(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        self.assertEqual(tenDollars, fiveDollars.times(2))

    def testMultiplicationInEuros(self):
        tenEuros = Money(10, "EUR")
        twentyEuros = Money(20, "EUR")
        self.assertEqual(twentyEuros, tenEuros.times(2))

    def testDivision(self):
        originalMoney = Money(4002, "KRW")
        actualMoneyAfterDivision = originalMoney.divide(4)
        expectedMoneyAfterDivision = Money(1000.5, "KRW")
        self.assertEqual(expectedMoneyAfterDivision, actualMoneyAfterDivision)

    def testAddition(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portofolio = Portofolio()
        portofolio.add(fiveDollars, tenDollars)
        self.assertEqual(fifteenDollars, portofolio.evaluate("USD"))

    def testAdditionOfDollarsAndEuros(self):
        fiveDollars = Money(5, "USD")
        tenEuros = Money(10, "EUR")
        portofolio = Portofolio()
        portofolio.add(fiveDollars, tenEuros)
        expectedValue = Money(17, "USD")
        actualValue = portofolio.evaluate("USD")
        self.assertEqual(expectedValue, actualValue,
                        "%s != %s"%(expectedValue, actualValue))

    def testAdditionOfDollasAndnWons(self):
        oneDollar = Money(1, "USD")
        elevenHundredWon = Money(1100, "KRW")
        portofolio = Portofolio()
        portofolio.add(oneDollar, elevenHundredWon)
        expectedValue = Money(2200, "KRW")
        actualValue = portofolio.evaluate("KRW")
        self.assertEqual(expectedValue, actualValue,
                        "%s != %s"%(expectedValue, actualValue))
    

if __name__ == '__main__':
    unittest.main()
