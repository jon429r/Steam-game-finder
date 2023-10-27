'''HomePage/models.py:
This file is used to define the data models for your app. 
Models define the structure of your database tables and the relationships between tables.'''
from django.db import models

# Create your models here.
##TODO: Add the rest of the fields

class Game(models.Model):
    title = models.CharField(max_length=200)


class Language(models.Model):
    language = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

class Developer(models.Model):
    developer = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

class Publisher(models.Model):
    publisher = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

