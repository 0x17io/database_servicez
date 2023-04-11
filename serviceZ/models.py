from django.db import models

# Create your models here.

class Account (models.Model):
    PersonID = models.IntegerField()
    FirstName = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.PersonID} is {self.FirstName}"
    class Meta:
        db_table = "Account"
