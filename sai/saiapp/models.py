from django.db import models
from django.utils import timezone
# Create your models here.
from datetime import datetime
class pkid(models.Model):
    idg=models.AutoField(primary_key=True)
class register1(models.Model):
    rgid=models.AutoField(primary_key=True)
    rid=models.CharField(max_length=20)
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    dob=models.DateField()
    address=models.CharField(max_length=250)
    blood_group=models.CharField(max_length=25)
    email=models.EmailField()
    creates=models.DateField(default=timezone.now())
    number=models.CharField(max_length=25)
    def __str__(self):
        return self.name
    def set_id(self):
        super().save()
        a=self.creates.strftime('%d')
        b=self.creates.strftime('%m')
        c=self.rgid
        f=str(c)
        e=self.gender[:1].upper()
        d='SSSOT-'
        return d+a+b+e+f
    def save(self):
        self.rid=self.set_id()
        return super().save()