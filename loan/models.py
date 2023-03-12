from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class InvestorAccount(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="account_owner")
    account_id = models.IntegerField(null=True)
    account_cash = models.DecimalField(decimal_places=2,max_digits=7)

class BorrowerAccount(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="borrower_account")

class LoanRequest(models.Model):
    borrower = models.ForeignKey(BorrowerAccount, on_delete=models.DO_NOTHING, related_name="MoneyBorrower")
    amount_borrowing = models.DecimalField(decimal_places=2,max_digits=7)
    investment_interest = models.DecimalField(decimal_places=2,max_digits=7)
    minimum_investment = models.DecimalField(decimal_places=2,max_digits=7)
    payment_period_start = models.DateField()
    payement_period_end = models.DateField()
    active = models.BooleanField()

class LoanShare(models.Model):
    for_loan = models.ForeignKey(LoanRequest, on_delete=models.DO_NOTHING, related_name="loan_invested_in")
    amount = models.DecimalField(decimal_places=2,max_digits=7)
    processed = models.BooleanField()

class LoanPayment(models.Model):
    loan = models.ForeignKey(BorrowerAccount, on_delete=models.DO_NOTHING, related_name="loanPayingFor")
    paymentID = models.UUIDField()
    payment_date = models.DateField()
    payment_amount = models.DecimalField(decimal_places=2,max_digits=7)
    paid = models.BooleanField()