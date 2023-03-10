# Generated by Django 4.1.3 on 2023-03-01 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investoraccount',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='loanpayment',
            name='loan',
        ),
        migrations.RemoveField(
            model_name='loanrequest',
            name='borrower',
        ),
        migrations.RemoveField(
            model_name='loanshare',
            name='for_loan',
        ),
        migrations.DeleteModel(
            name='BorrowerAccount',
        ),
        migrations.DeleteModel(
            name='InvestorAccount',
        ),
        migrations.DeleteModel(
            name='LoanPayment',
        ),
        migrations.DeleteModel(
            name='LoanRequest',
        ),
        migrations.DeleteModel(
            name='LoanShare',
        ),
    ]
