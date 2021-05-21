from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
    meetingid=models.IntegerField
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField
    meetingtime=models.TimeField
    location=models.CharField(max_length=255)
    agenda=models.TextField(null=True, blank=True)

def __str__(self):
    return self.meetingid

class Meta:
    db_table='meeting'
    verbose_name_plural='meeting'

class MeetingMinutes(models.Model):
    meeting=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutes=models.TextField

def __str__(self):
    return self.meetingid

class Meta:
    db_table='MeetingMinutes'
    verbose_name_plural='MeetingMinutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    url=models.URLField
    dateentered=models.DateField
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.TextField()

    def discountAmount(self):
        self.discount=self.price * .05
        return self.discount

    def discountPrice(self):
        disc=self.discountAmount()
        self.discountPrice=self.price-self.disc

def __str__(self):
    return self.resourcename

class Meta:
    db_table='resource'
    verbose_name_plural='resource'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    date=models.DateField
    time=models.TimeField
    description=models.TextField

def __str__(self):
    return self.meetingtitle

class Meta:
    db_table='event'
    verbose_name_plural='event'