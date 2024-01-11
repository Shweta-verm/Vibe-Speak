from django.db import models



# Create your models here.
class signin(models.Model):
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
class signup(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
    repassword=models.CharField(max_length=122)
    
class contact_us(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length=100, default='Not available' )
    message = models.CharField(max_length=2000)

