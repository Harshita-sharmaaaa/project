from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=20)
    father_name=models.CharField(max_length=40)
    email=models.CharField(max_length=50)
    feedback=models.CharField(max_length=200)
    
class subscribe(models.Model):
    email=models.CharField(max_length=50)
    class Meta:
        db_table="subscribe"
    def str(self):
        return self.email
    

class subsc(models.Model):
    email=models.CharField(max_length=50)
    def str(self):
        return self.email