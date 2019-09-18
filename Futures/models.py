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
