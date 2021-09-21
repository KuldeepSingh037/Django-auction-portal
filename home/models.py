from django.db import models
from auction.models import seller
from login.models import credentials

# Create your models here.


class complete(models.Model):
    buyer=models.IntegerField(default=0)
    seller=models.IntegerField(default=0)
    name=models.CharField(max_length=50)
    category=models.CharField(max_length=20)
    size=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    bidamnt=models.IntegerField(default=0)
    date=models.DateField('date')
    description=models.CharField(max_length=200)
    contact=models.CharField(max_length=15)
    document=models.ImageField(upload_to='property_details')
    pic1=models.ImageField(upload_to='property_details')
    pic2=models.ImageField(upload_to='property_details')
    pic3=models.ImageField(upload_to='property_details')
    pic4=models.ImageField(upload_to='property_details')


class bidder(models.Model):
    bid=models.ForeignKey(seller, on_delete=models.CASCADE)
    cid=models.ForeignKey(credentials, on_delete=models.CASCADE)
    amnt=models.IntegerField(default=0)
