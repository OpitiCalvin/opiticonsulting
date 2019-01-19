from django.db import models

# Create your models here.

class Demo(models.Model):
    title = models.CharField('Title', max_length=30)
    brief = models.TextField('Short Brief', max_length=200)
    link = models.CharField('Demo Url', max_length=50, blank=True)
    thumbnail = models.ImageField(upload_to='solution/', blank=True)
    
    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField('Title', max_length=30)
    brief = models.TextField('Short Brief', max_length=200)
    link = models.CharField('Service Url', max_length=50, blank=True)
    thumbnail = models.ImageField(upload_to='service/', blank=True)
    
    def __str__(self):
        return self.title 

class Contact(models.Model):
    name = models.CharField('Names', max_length= 50)
    phone = models.CharField('Phone Contact', max_length=15, blank=True)
    email = models.EmailField('E-Mail')
    city = models.CharField('City', max_length=25, blank=True)
    country = models.CharField('Country', max_length=25, blank=True)
    title = models.CharField('Title', max_length=30)
    message = models.TextField('Message')

    def __str__(self):
        return self.name
    
