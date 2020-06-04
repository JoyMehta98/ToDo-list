from __future__ import unicode_literals
from djongo import models

# Create your models here.

class Todo(models.Model):
    id = models.IntegerField(primary_key = True)
    added_date = models.DateTimeField()
    text = models.CharField(max_length = 350)

    