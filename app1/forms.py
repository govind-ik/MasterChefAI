from django import forms

class recipe(forms.Form):
    recipe_name=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder':'Ask your recipe'}))
