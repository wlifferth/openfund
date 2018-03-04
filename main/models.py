from django.db import models

# Create your models here.
# Create your models here.
class UserProfile(models.Model):
    name = models.CharField("Name", max_length=100)
    email = models.EmailField("Email")
    passwordHash = models.CharField("Password", max_length=100)
    generalGoals = models.TextField(blank=True)
    targetAmount = models.FloatField("Target Amount", default=0)
    targetDate = models.DateField("Target Date", auto_now=True)
    targetContribution = models.FloatField("Target Contribution", default=0)
    riskTolerance = models.FloatField("Risk Tolerance", default=0)
    tags = models.TextField(blank=True)

    def add_tag(self, new_tag):
        tags = self.tags.split(':')
        if new_tag not in tags:
            tags.append(new_tag)
        tags = ':'.join(tags)

    def get_tags(self):
        return self.tags.split(':')

    def __str__(self):
        return "UserProfile({})".format(self.name)

class PortfolioEntry(models.Model):
    ticker = models.CharField("Ticker Symbol", max_length=100)
    quantity = models.FloatField("Quantity")
    price = models.FloatField("Price")
    time = models.DateTimeField("Time Placed", auto_now=True)

    def __str__(self):
        return "PortfolioEntry({} shares of {}@${}/share)".format(self.quantity, self.ticker, self.price)

class Trade(models.Model):
    SIDE = [('BUY', 'Buy'), ('SELL', 'Sell')]
    ticker = models.CharField("Ticker Symbol", max_length=100)
    side = models.CharField(max_length=2, choices=SIDE, default='BUY')
    USDQuantity = models.FloatField("USD Quantity")
    time = models.DateTimeField("Time Placed", auto_now=True)
    algorithmName = models.CharField("Algorithm Name", max_length=100)

    def __str__(self):
        return "Trade({} {} shares of {})".format(self.side, self.USDQuantity, self.ticker)

class Algorithm(models.Model):
    name = models.CharField("Algorithm Name", max_length=100)
    description = models.TextField("Algorithm Description")
    averageReturnHigh = models.FloatField("Average Return (high)")
    averageReturnLow = models.FloatField("Average Return (low)")
    appSlug = models.CharField("App Slug", max_length=100)
    period = models.IntegerField("Period between trades")

    def __str__(self):
        return "Algorithm({})".format(self.name)
