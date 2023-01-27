from django import forms
from django.forms import ModelForm
from .models import TutorialCategory
# from django.form import ModelForm


list1 = (
        ('a','a'),
        ('b','b'),
        ('c','c'),
    )

days_s= [(10,10),(50,50),(100,100),(500,500)]
class search_day(forms.Form) :
    stock = forms.ChoiceField(choices=days_s)


class Form(ModelForm):
    # tutorial_category = forms.ChoiceField(choices=list1)
    class Meta:
        model = TutorialCategory
        fields = [
            'tutorial_category' ,
            
        ]
        