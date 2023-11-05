from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from datetime import datetime
import django.core.exceptions as Exceptions
import django.db.utils as dbExceptions

class Filter(models.Model):
    try:
        DepartureDate  = models.DateField( "DepartureDate",  null = False, blank = False)
        ReturnDate = models.DateField( "ReturnDate", null = False, blank = False)
        #Destination = destinationField()
        City = models.CharField('City', max_length= 30, null = False, blank = False)
        State = models.CharField('State',max_length= 30, null = False, blank = False)
        Country = models.CharField('Country', max_length= 30,null = False, blank = False)
        NumberOfTraveler = models.IntegerField('NumberOfTraveler',null = False, blank = False)
        BudgeMin = models.IntegerField('BudgeMin' )
        BudgetMax = models.IntegerField('BudgetMax',null = False, blank = False)

    except Exceptions.ValidationError:
        print("date format must be in YYYY-MM-DD format.'")
    
    except dbExceptions.IntegrityError:
        print("Must input all required values")


    def __str__(self):
        return self.DepartureDate.strftime("%m/%d/%Y") + "-" + self.ReturnDate.strftime("%m/%d/%Y") + ", " + self.City + " " + self.State
    
