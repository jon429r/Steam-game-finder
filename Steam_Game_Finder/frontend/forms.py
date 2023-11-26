from django import forms

class LikeDislikeForm(forms.Form):
    game_id = forms.IntegerField()
    action = forms.CharField()