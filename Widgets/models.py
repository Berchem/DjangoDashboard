# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Chat(models.Model):
    index = models.IntegerField(primary_key=True)
    user = models.TextField(blank=False, null=False)
    datetime = models.TextField(blank=False, null=False)
    msg = models.TextField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'chat'


class ToDoList(models.Model):
    index = models.IntegerField(primary_key=True)
    item = models.TextField(blank=False, null=False)
    status = models.IntegerField(blank=False, null=False)
    user = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'to_do_list'
