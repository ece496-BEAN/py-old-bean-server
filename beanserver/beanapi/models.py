from django.db import models


class Expense(models.Model):
    # transaction_datetime = models.DateTimeField()
    # payee = models.CharField(max_length=100)
    # category = models.CharField(max_length=100)
    cost = models.FloatField()
    # user_notes = models.TextField()

    # class Meta:
        # ordering = ["transaction_datetime"]

