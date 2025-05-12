from django.db import models
from django.contrib import admin


class Movie(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
    director = models.CharField(max_length=10)
    hero = models.CharField(max_length=10)
    your_rating = models.IntegerField()

class Movieadmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'hero', 'your_rating')