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
