from django import forms
from .models import Game

class LikeDislikeForm(forms.Form):
    game_id = forms.IntegerField()
    action = forms.CharField()

class SearchForm(forms.Form):
    search = forms.CharField(required=True, max_length=100)
    filter = [
        ('title', 'Title'),
        ('genre', 'Genre'),
        ('developer', 'Developer'),
        ('publisher', 'Publisher'),
    ]

