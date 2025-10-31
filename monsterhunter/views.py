from django.shortcuts import render,redirect,get_object_or_404
#import the model:
from .models import Monster
#import the forms.py so we can give it logic:
from .forms import MonsterForm
#import the message for error handling:
from django.contrib import messages
#import the request library for handling publick API:
import requests
# Create your views here.
#create a function that lets the user create their own monster:
def create_monster(request):
    #check if the request is a post:
    if request.method == "POST":
        #fill the form with the data the user input:
        form = MonsterForm(request.POST)
        #check if the form fields are valid(non-empty,correct type,etc):
        if form.is_valid():
            #save it to our DB:
            form.save()
            #after creating send the user back to the monster list:
            return redirect("monster-list")
        
#create a function for storing the monsters:
def monster_list(request):
    #store all the monsters in a variable:
    monsters = Monster.objects.all()
    #tell it which folder and file html to render the list:
    return render(request,"monsterhunter/monster_list.html",{"monsters":monsters})