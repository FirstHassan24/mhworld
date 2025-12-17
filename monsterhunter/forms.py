#import forms so django know what your trying to do:
from django import forms
#import the monster model so the user can add values to the fields:
from .models import Monster,Item

#create the form that the user will be using to input data:
class MonsterForm(forms.ModelForm):
    #tell django which model to use and how to configure the form:
    class Meta:
        #asscociate this form with your monster model:
        model = Monster
        #(make sure their fields match)
        fields = ["name","species","elements","description"]

#create the item form for the item view to use:
class ItemForm(forms.ModelForm):
    #tell DJango which model to use and how to configure the form:
    class meta:
        #asscociate this form with my Item model:
        model = Item
        #make sure the fields match:
        fields = ['name',"description","value","rarity"]