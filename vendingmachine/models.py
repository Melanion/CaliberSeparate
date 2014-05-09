from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User)

    balance = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return self.user.username

class Caliber(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Purpose(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class GoodFor(models.Model):
    caliber = models.ForeignKey(Caliber)
    purpose = models.ForeignKey(Purpose)

    def __unicode__(self):
        return self.purpose.name

class Bullet(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField(max_length=3)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    manufacturer = models.CharField(max_length=50)
    caliber = models.ForeignKey(Caliber)

    def __unicode__(self):
        return self.name