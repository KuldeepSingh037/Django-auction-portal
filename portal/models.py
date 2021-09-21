from django.db import models
from login.models import credentials

# Create your models here.

class seller(models.Model):
    cid=models.ForeignKey(credentials, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    category=models.CharField(max_length=20)
    size=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    minamnt=models.IntegerField(default=0)
    date=models.DateField('date')
    description=models.CharField(max_length=200)
    contact=models.CharField(max_length=15)
    document=models.ImageField(upload_to='property_details')
    pic1=models.ImageField(upload_to='property_details')
    pic2=models.ImageField(upload_to='property_details')
    pic3=models.ImageField(upload_to='property_details')
    pic4=models.ImageField(upload_to='property_details')

    