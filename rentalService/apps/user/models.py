from django.db import models

# Create your models here.
class User(models.Model):
	id = models.AutoField(primary_key=True)
	postCode = models.CharField(max_length=8)
	address = models.CharField(max_length=256)
	phone = models.CharField(max_length=11)
	grade = models.IntegerField(null=True)
	accountInfo = models.CharField(max_length=128, blank=True)
	userInfo = models.CharField(max_length=128, blank=True)