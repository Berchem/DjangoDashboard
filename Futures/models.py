from django.db import models


class HModel(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.TextField()
    weighted_index = models.TextField()
    volume = models.TextField()
    current_price = models.TextField()
    next_price = models.TextField()

    class Meta:
        managed = False
        db_table = 'h_model'


class TestKLineData(models.Model):
    index = models.IntegerField(primary_key=True)
    item_code = models.TextField(blank=True, null=True)
    datetime = models.TextField(blank=True, null=True)
    open = models.TextField(blank=True, null=True)
    high = models.TextField(blank=True, null=True)
    low = models.TextField(blank=True, null=True)
    close = models.TextField(blank=True, null=True)
    volume = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_k_line_data'


class TestQuoteData(models.Model):
    index = models.IntegerField(primary_key=True)
    item_code = models.TextField(blank=True, null=True)
    datetime = models.TextField(blank=True, null=True)
    open = models.TextField(blank=True, null=True)
    high = models.TextField(blank=True, null=True)
    low = models.TextField(blank=True, null=True)
    close = models.TextField(blank=True, null=True)
    volume = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_quote_data'


class TestTicksData(models.Model):
    index = models.IntegerField(primary_key=True)
    sstockidx = models.TextField(db_column='sStockIdx', blank=True, null=True)  # Field name made lowercase.
    nptr = models.TextField(db_column='nPtr', blank=True, null=True)  # Field name made lowercase.
    datetime = models.TextField(blank=True, null=True)
    nbid = models.TextField(db_column='nBid', blank=True, null=True)  # Field name made lowercase.
    nask = models.TextField(db_column='nAsk', blank=True, null=True)  # Field name made lowercase.
    nclose = models.TextField(db_column='nClose', blank=True, null=True)  # Field name made lowercase.
    nqty = models.TextField(db_column='nQty', blank=True, null=True)  # Field name made lowercase.
    nsimulate = models.TextField(db_column='nSimulate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test_ticks_data'
