from django.test import TestCase
from .models import UserProfile
from .updateUserProfile import convertToFirstTime, updateUserProfile
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

class UpdateUserProfileTestCase(TestCase):
    def setUp(self):
        self.user = UserProfile(name="William Lifferth", email="wlifferth@icloud.com", passwordHash="12345")
        self.user.save()
        self.data = {
            'generalGoals' : "Goals goals goals!",
            'currentSavings': '2000',
            'currentTakehome': '2000',
            'currentDebt': '2000',
            'targetContribution': '200',
            'married': 'off',
            'currentChildren': '0',
            'childSoon': 'on',
            'healthProblems': 'off',
            'retirement': 'on',
            'retirementTime': '50',
            'retirementTargetAmount': '100000',
            'bigTicket': 'on',
            'bigTicketTime': '6',
            'bigTicketTargetAmount': '20000',
            'questionOne': '4',
            'questionTwo': '2',
            'questionThree': '0',
        }
    def test_updateUserProfile_works(self):
        updateUserProfile(self.user, self.data)
