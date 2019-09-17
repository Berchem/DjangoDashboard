from django.db import models


class CapitalAccount(models.Model):
    index = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=30)
    account = models.TextField(max_length=7)
    id_number = models.CharField(max_length=10)
    password = models.CharField(max_length=128)
    deposit_code = models.CharField(max_length=3)
    deposit_account = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'capital_account'


class CapitalFuturesCorp(models.Model):
    index = models.IntegerField(primary_key=True)
    bank = models.CharField(max_length=128)
    code = models.CharField(max_length=3)
    prefix = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'capital_futures_corp'
