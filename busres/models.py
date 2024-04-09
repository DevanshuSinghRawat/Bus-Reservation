from django.db import models
from django import forms

class Booking(models.Model):
    
    busName = models.CharField(max_length=15)
    busType = models.CharField(max_length=10)
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    seats = models.IntegerField()
    price = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

class UsersData(models.Model):
    userid = models.CharField(max_length=30 , primary_key = True)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

class UserBookings(models.Model):
    STATUS_CHOICES = (('Booked', 'booked'),
                      ('Cancled', 'cancled'))
    userid = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    booking_id = models.ForeignKey( Booking, on_delete=models.CASCADE )
    req_seats = models.IntegerField(default =1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES )

class CurrentUser(models.Model):
    userid = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)