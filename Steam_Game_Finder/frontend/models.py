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
class Popular_Games(models.Model):
    app_id = models.AutoField(primary_key=True, default=None)
    title = models.CharField(max_length=255, default=None, blank=True, null=True)
    header_image = models.URLField(default=None, blank=True, null=True)
    action = models.CharField(max_length=200, default=None, blank=True, null=True)

    def __str__(self):
        return self.title
    
class Resulting_Games(models.Model):
    app_id = models.AutoField(primary_key=True, default=None)
    title = models.CharField(max_length=255, default=None, blank=True, null=True)
    header_image = models.URLField(default=None, blank=True, null=True)
    action = models.CharField(max_length=200, default=None, blank=True, null=True)

    def __str__(self):
        return self.title


class Liked_Disliked(models.Model):
    app_id = models.AutoField(primary_key=True, default=None)
    title = models.CharField(max_length=255, default=None, blank=True, null=True)
    header_image = models.URLField(default=None, blank=True, null=True)
    action = models.CharField(max_length=200, default=None, blank=True, null=True)

    def __str__(self):
        return self.title
    
class Game(models.Model):
    app_id = models.AutoField(primary_key=True, default=None)
    name = models.CharField(max_length=210, default=None, blank=True, null=True)
    release_date = models.CharField(max_length=200, default=None, blank=True, null=True)
    required_age = models.IntegerField(default=0, null=True, blank=True)
    price = models.FloatField(default=0.0, null=True, blank=True)
    about_the_game = models.TextField(default=None, blank=True, null=True)
    supported_languages = models.TextField(default=None, blank=True, null=True)
    header_image = models.URLField(default=None, blank=True, null=True)
    windows = models.BooleanField(default=False, null=True, blank=True)
    mac = models.BooleanField(default=False, null=True, blank=True)
    linux = models.BooleanField(default=False, null=True, blank=True)
    metacritic_score = models.IntegerField(null=True, blank=True)
    positive = models.IntegerField(default=0, null=True, blank=True)
    negative = models.IntegerField(default=0, null=True, blank=True)
    categories = models.TextField(default=None, blank=True, null=True)
    genres = models.TextField(default=None, blank=True, null=True)
    tags = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    app_id = models.CharField(max_length=260, default=None, blank=True, null=True)
    language = models.CharField(max_length=200, default=None, blank=True, null=True)

    def __str__(self):
        return self.language

class Developer(models.Model):
    app_id = models.CharField(max_length=260, default=None, blank=True, null=True)
    developer = models.CharField(max_length=200, default=None, blank=True, null=True)

    def __str__(self):
        return self.developer

class Publisher(models.Model):
    app_id = models.CharField(max_length=260, default=None, blank=True, null=True)
    publisher = models.CharField(max_length=200, default=None, blank=True, null=True)

    def __str__(self):
        return self.publisher
