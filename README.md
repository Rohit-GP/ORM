# Ex02 Django ORM Web Application
## Date: 12-05-2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 8 Movies.

## PROGRAM


```
admin.py 

from django.contrib import admin
from .models import Movie,Movieadmin
admin.site.register(Movie,Movieadmin)

models.py

from django.db import models
from django.contrib import admin

class Movie(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
    director = models.CharField(max_length=10)
    hero = models.CharField(max_length=10)
    your_rating = models.IntegerField()

class Movieadmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'hero', 'your_rating')
```

## OUTPUT

![output](<Screenshot 2025-05-12 111319.png>)

## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
