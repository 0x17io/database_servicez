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

class Background (models.Model):

    # Main attributes
    ID = models.IntegerField()
    HasCharges = models.BooleanField()
    Charges = models.CharField(max_length=250)

    class Meta:
        db_table = "Background"

class AdminRoles (models.Model):

    # main attributes
    RoleID = models.IntegerField()
    Type = models.CharField(max_length=250)
    Description = models.CharField(max_length=250)

    class Meta:
        db_table = "AdminRoles"

class Administrator (models.Model):

    # Main attributes
    ID = models.IntegerField()
    RoleID = models.IntegerField()

    class Meta:
        db_table = "Administrator"

class Clients (models.Model):

    # Main attributes
    ID = models.IntegerField()
    ClientID = models.IntegerField()

    class Meta:
        db_table = "Clients"

class Contractors (models.Model):

    # Main attributes
    ID = models.IntegerField()
    ContractorID = models.IntegerField()
    ServiceID = models.IntegerField()
    Availability = models.BooleanField()

    class Meta:
        db_table = "Contractors"


class Services (models.Model):
    # Main attributes
    ServiceID = models.IntegerField()
    TypeID = models.IntegerField()
    Description = models.CharField(max_length=250)
    Rate = models.FloatField()

    class Meta:
        db_table = "Services"

class ServiceTypes (models.Model):
    # Main attributes
    TypeID = models.IntegerField()
    Type = models.CharField(max_length=250)

    class Meta:
        db_table = "ServiceTypes"

class Requests (models.Model):
    # Main attributes
    RequestID = models.IntegerField()
    ClientID = models.IntegerField()
    ServiceID = models.IntegerField()
    Timestamp = models.DateTimeField()

    class Meta:
        db_table = "Requests"


class Reviews (models.Model):
    # Main attributes
    ReviewID = models.IntegerField()
    ClientID = models.IntegerField()
    ContractorID = models.IntegerField()
    Rating = models.IntegerField()
    Comment = models.CharField(max_length=250)

    class Meta:
        db_table = "Reviews"


class Transactions (models.Model):
    # Main attributes
    TransID = models.IntegerField()
    ClientID = models.IntegerField()
    ContractorID = models.IntegerField()
    AmountPaid = models.FloatField()
    Timestamp = models.DateTimeField()

    class Meta:
        db_table = "Transactions"

class Orders (models.Model):
    # Main attributes
    OrderID = models.IntegerField()
    ClientID = models.IntegerField()
    ContractorID = models.IntegerField()
    TransactionID = models.IntegerField()
    Timestamp = models.DateTimeField()

    class Meta:
        db_table = "Orders"