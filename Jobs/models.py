from django.db import models


# Create your models here.
class TestRequestJob(models.Model):
    index = models.IntegerField(primary_key=True)
    username = models.TextField(blank=True, null=True)
    submit_time = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    program = models.TextField(blank=True, null=True)
    process = models.TextField(blank=True, null=True)
    item_code = models.TextField(blank=True, null=True)
    page = models.TextField(blank=True, null=True)
    k_line_type = models.TextField(blank=True, null=True)
    output_format = models.TextField(blank=True, null=True)
    trade_session = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_request_job'


class TestRequestJobDaily(models.Model):
    index = models.IntegerField(primary_key=True)
    username = models.TextField(blank=True, null=True)
    submit_time = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    program = models.TextField(blank=True, null=True)
    process = models.TextField(blank=True, null=True)
    item_code = models.TextField(blank=True, null=True)
    page = models.TextField(blank=True, null=True)
    k_line_type = models.TextField(blank=True, null=True)
    output_format = models.TextField(blank=True, null=True)
    trade_session = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_request_job_daily'

