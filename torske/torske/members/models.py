from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address1 = models.CharField(max_length=40, blank=True)
    address2 = models.CharField(max_length=40, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=30, blank=True)
    winteraddress1 = models.CharField(max_length=40, blank=True)
    winteraddress2 = models.CharField(max_length=40, blank=True)
    wintercity = models.CharField(max_length=60, blank=True)
    winterstate = models.CharField(max_length=30, blank=True)
    occupation = models.CharField(max_length=40, blank=True)
    businessname = models.CharField(max_length=60, blank=True)
    businessaddr1 = models.CharField(max_length=60, blank=True)
    businessaddr2 = models.CharField(max_length=60, blank=True)
    businesscity = models.CharField(max_length=30, blank=True)
    businessstate = models.CharField(max_length=30, blank=True)
    wifename = models.CharField(max_length=60, blank=True)
    email1 = models.EmailField(blank=True)
    email2 = models.EmailField(blank=True)
    pic = models.ImageField(upload_to='/static/images', blank=True)
    active = models.BooleanField()
    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    year1 = models.CharField(max_length=30, blank=True)
    year2 = models.CharField(max_length=30, blank=True)
    year3 = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    
    
    