from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
