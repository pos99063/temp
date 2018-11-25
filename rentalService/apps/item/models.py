from django.db import models
from apps.user.models import RealUser
# Create your models here.

class Item(models.Model):
    ## AUTO
    id = models.AutoField(primary_key=True)
    registDate = models.DateField(auto_now=True)

    ## NULLABLE
    status = models.IntegerField(null=True)  # ?

    ## NOT NULL
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(RealUser, on_delete=models.CASCADE)

    price = models.IntegerField()
    minRentDay = models.IntegerField()
    maxRentDay = models.IntegerField()
    picture = models.ImageField(blank=True, upload_to='images/%Y/%m-%d', max_length=128)
    info = models.TextField()



