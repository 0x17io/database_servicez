from django.db import models

# Create your models here.


class Account (models.Model):

    # Main attributes
    ID = models.IntegerField()
    FirstName = models.CharField(max_length=250)
    LastName = models.CharField(max_length=250)
    EmailAddr = models.CharField(max_length=250)
    Zipcode = models.IntegerField()
    Language = models.CharField(max_length=250)
    class Meta:
        db_table = "Account"
