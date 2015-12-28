from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address1 = models.CharField(max_length=40, blank=True, null=True)
    address2 = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=60, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    winteraddress1 = models.CharField(max_length=40, blank=True, null=True)
    winteraddress2 = models.CharField(max_length=40, blank=True, null=True)
    wintercity = models.CharField(max_length=60, blank=True, null=True)
    winterstate = models.CharField(max_length=30, blank=True, null=True)
    occupation = models.CharField(max_length=40, blank=True,null=True)
    businessname = models.CharField(max_length=60, blank=True, null=True)
    businessaddr1 = models.CharField(max_length=60, blank=True, null=True)
    businessaddr2 = models.CharField(max_length=60, blank=True, null=True)
    businesscity = models.CharField(max_length=30, blank=True, null=True)
    businessstate = models.CharField(max_length=30, blank=True, null=True)
    wifename = models.CharField(max_length=60, blank=True, null=True)
    email1 = models.EmailField(blank=True, null=True)
    email2 = models.EmailField(blank=True, null=True)
    pic = models.ImageField(upload_to='/static/images', blank=True, null=True)
    active = models.BooleanField()
    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    year1 = models.CharField(max_length=30, blank=True, null=True)
    year2 = models.CharField(max_length=30, blank=True, null=True)
    year3 = models.CharField(max_length=30, blank=True, null=True)
    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    
    
    