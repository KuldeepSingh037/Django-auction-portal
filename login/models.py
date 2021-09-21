from django.db import models

# Create your models here.

class credentials(models.Model):
    name=models.CharField(max_length=100)
    userpic=models.ImageField(upload_to='user_details',default='0')
    email=models.EmailField(default='0')
    mbno=models.CharField(max_length=15,default='0')
    adhaarno=models.CharField(max_length=17, default='0')
    city=models.CharField(max_length=50,default='beawar')
    fadhaar=models.ImageField(upload_to='user_details',default='0')
    badhaar=models.ImageField(upload_to='user_details',default='0')
    pwd=models.CharField(max_length=20)
    gender=models.CharField(max_length=11, default=0)




