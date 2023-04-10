from django.db import models

# Create your models here.

class account(models.Model):
    person_id = models.IntegerField()
    first_name = models.CharField(max_length=250)
