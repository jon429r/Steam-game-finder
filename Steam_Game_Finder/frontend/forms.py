from django import forms
from .models import Game

class LikeDislikeForm(forms.Form):
    game_id = forms.IntegerField()
    action = forms.CharField()

class SearchForm(forms.Form):
    search_term = forms.CharField(required=True)
    field_choice = forms.CharField(required=True) 
    filter = [
        ('name', 'Name'),
        ('genre', 'Genre'),
        ('developer', 'Developer'),
        ('publisher', 'Publisher'),
        ('recommendation', 'Recommendation'),
        ('devoloper_by_reception', 'Developer_by_Reception'),
    ]

