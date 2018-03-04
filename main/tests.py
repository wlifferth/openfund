from django.test import TestCase
from .updateUserProfile import convertToFirstTime
from datetime import date, timedelta

# Create your tests here.
class TimeValueTestCase(TestCase):
    def setUp(self):
        self.time1 = date(year=2010, month=1, day=1)
        self.time2 = date(year=2005, month=1, day=1)
        self.interestRate = 0.05
        self.amount1 = 1000
        self.amount2 = 2000

    def test_tvm_works(self):
        time, amount = convertToFirstTime(self.time1, self.amount1, self.time2, self.amount2, self.interestRate)
        self.assertEqual(time, date(year=2005, month=1, day=1))
        self.assertAlmostEqual(amount, 2783.5261664684588, places=1)
