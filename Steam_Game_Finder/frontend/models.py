'''HomePage/models.py:
This file is used to define the data models for your app. 
Models define the structure of your database tables and the relationships between tables.'''
from django.db import models

# Create your models here.

"""AppID, Name, Release date, Required Age, Price, 
About the game, Supported Languages, Header Image, 
Windows, Mac, Linux, Metacritic Score, Positive, 
Negative, Devolopers, Publishers, Categories, Genres, Tags
"""


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=200, default=None, blank=True, null=True)

    def __str__(self):
        return self.language

class Developer(models.Model):
    id = models.AutoField(primary_key=True)
    developer = models.CharField(max_length=200, default=None, blank=True, null=True)

    def __str__(self):
        return self.developer

class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    publisher = models.CharField(max_length=200, default=None, blank=True, null=True)

    def __str__(self):
        return self.publisher

class Game(models.Model):
    app_id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200, default=None, blank=True, null=True)
    release_date = models.CharField(max_length=200, default=None, blank=True, null=True)
    required_age = models.IntegerField(default=0, null=True, blank=True)
    price = models.FloatField(default=0.0, null=True, blank=True)
    about_the_game = models.TextField(default=None, blank=True, null=True)
    supported_languages = models.ManyToManyField(Language, blank=True)
    header_image = models.URLField(default=None, blank=True, null=True)
    windows = models.BooleanField(default=False, null=True, blank=True)
    mac = models.BooleanField(default=False, null=True, blank=True)
    linux = models.BooleanField(default=False, null=True, blank=True)
    metacritic_score = models.IntegerField(null=True, blank=True)
    positive = models.IntegerField(default=0, null=True, blank=True)
    negative = models.IntegerField(default=0, null=True, blank=True)
    developers = models.ManyToManyField(Developer, blank=True)
    publishers = models.ManyToManyField(Publisher, blank=True)
    categories = models.TextField(default=None, blank=True, null=True)
    genres = models.TextField(default=None, blank=True, null=True)
    tags = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name
