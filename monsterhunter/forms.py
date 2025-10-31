#import forms so django know what your trying to do:
from django import forms
#import the monster model so the user can add values to the fields:
from .models import Monster

#create the form that the user will be using to input data:
class MonsterForm(forms.ModelForm):
    #tell django which model to use and how to configure the form:
    class Meta:
        #asscociate this form with your monster model:
        model = Monster
        fields = "__all__"
        