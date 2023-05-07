from django.db import models
from django.contrib.auth.models import AbstractUser
class Account(AbstractUser):

    is_anonymous = False
    is_authenticated = True

    FirstName = models.CharField(max_length=250)
    LastName = models.CharField(max_length=250)
    EmailAddr = models.CharField(max_length=250)

    Zipcode = models.IntegerField(default=0)
    Language = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = "Account"

class Background (models.Model):

    # Main attributes
    #BackgroundID =  models.AutoField(primary_key=True)
    HasCharges = models.BooleanField()
    Charges = models.CharField(max_length=250)

    class Meta:
        db_table = "Background"

class AdminRole (models.Model):

    # main attributes
    #RoleID =  models.AutoField(primary_key=True)
    Type = models.CharField(max_length=250)
    Description = models.CharField(max_length=250)

    class Meta:
        db_table = "AdminRoles"

class Administrator (models.Model):

    # Main attributes
    #AdministratorID =  models.AutoField(primary_key=True)
    RoleID = models.IntegerField()

    class Meta:
        db_table = "Administrator"

class ServiceType (models.Model):
    # Main attributes
    #TypeID =  models.AutoField(primary_key=True)
    Type = models.CharField(max_length=250)

    class Meta:
        db_table = "ServiceTypes"
class Service (models.Model):
    # Main attributes
    #ServiceID = models.AutoField(primary_key=True)
    TypeID = models.ForeignKey(ServiceType, on_delete=models.CASCADE, db_column='TypeID')
    Description = models.CharField(max_length=250)
    Rate = models.FloatField()

    class Meta:
        db_table = "Services"

class Client (models.Model):

    # Main attributes
    #ClientID = models.AutoField(primary_key=True)
    MainID = models.ForeignKey(Account, on_delete=models.CASCADE,db_column='MainID')


    class Meta:
        db_table = "Clients"

class Contractor (models.Model):

    # Main attributes
    #ContractorID = models.AutoField(primary_key=True)
    MainID = models.ForeignKey(Account, on_delete=models.CASCADE, db_column='MainID')

    ServiceID = models.ForeignKey(Service, on_delete=models.CASCADE, db_column='ServiceID')
    Availability = models.BooleanField()

    class Meta:
        db_table = "Contractors"

class Request (models.Model):
    # Main attributes
    #RequestID = models.AutoField(primary_key=True)
    ClientID = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='ClientID')
    ServiceID = models.ForeignKey(Service, on_delete=models.CASCADE, db_column='ServiceID')
    Timestamp = models.DateTimeField()

    class Meta:
        db_table = "Requests"


class Review (models.Model):
    # Main attributes
    #ReviewID = models.AutoField(primary_key=True)
    ClientID = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='ClientID')
    ContractorID = models.ForeignKey(Contractor, on_delete=models.CASCADE, db_column='ContractorID')
    Rating = models.IntegerField()
    Comment = models.CharField(max_length=250)

    class Meta:
        db_table = "Reviews"


class Transaction (models.Model):
    # Main attributes
    #TransID = models.AutoField(primary_key=True)
    ClientID = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='ClientID')
    ContractorID = models.ForeignKey(Contractor, on_delete=models.CASCADE, db_column='ContractorID')
    AmountPaid = models.FloatField()
    Timestamp = models.DateTimeField()

    class Meta:
        db_table = "Transactions"

class Order (models.Model):
    # Main attributes
    #OrderID = models.AutoField(primary_key=True)
    ClientID = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='ClientID')
    ContractorID = models.ForeignKey(Contractor, on_delete=models.CASCADE, db_column='ContractorID')
    TransactionID = models.ForeignKey(Transaction, on_delete=models.CASCADE, db_column='TransactionID')
    Timestamp = models.DateTimeField()

    class Meta:
        db_table = "Orders"