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
    #if the user is just visiting the page display the empty form model:
    else:
        #stores the form model in a variable
        form=MonsterForm()
        #render the form model inside the form template:
        return render(request,"monsterhunter/monster_form.html",{"form":form})
        
#create a function for storing the monsters:
def monster_list(request):
    #store all the monsters in a variable:
    monsters = Monster.objects.all()
    #tell it which folder and file html to render the list:
    return render(request,"monsterhunter/monster_list.html",{"monsters":monsters})

#create a function for updating each monster information:
def monster_update(request,pk):
    #find a monster by its pk by acessing the model or show not found:
    monster = get_object_or_404(Monster,pk=pk)
    #check if the user submited the form:
    if request.method == "POST":
        #bind the form to the posted data and existing instances:
        form = MonsterForm(request.POST, instance=monster)
        #validate the form:
        form.is_valid()
        #save the changes to the same row in the database:
        form.save()
        #create a message that tells you if you sucessfully updated:
        messages.success(request,"monster updated.")
        #after saving it return to the homepage:
        return redirect("monster-list")
    #show whats wrong when it fails:
    else:
        messages.error(request,"please fix this error")
        form = MonsterForm(instance=monster)
    #Render the same form template; pass a flag so we can change button text to “Update”:
        return render(request,"monsterhunter/monster_form.html",{"form":form,"is_edit":True})

#create a  function that delete a monster:
def delete_monster(request,pk):
    #store the value for each individual monster:
    monster = get_object_or_404(Monster,pk=pk)
    #if its a post request delete the monster:
    if request.method == "POST":
        #use the delete method to delete that monster:
        monster.delete()
        #return to the monster list:
        return redirect("monster-list")
    #show the confirmation page for get request:
    return render(request,"monsterhunter/monster_confirm_delete.html",{"monster":monster})

#create a function for importing monsters:
imported_monster = "https://mhw-db.com"
def import_monster(request):
    #if its not a post return to the list:
    if request.method != "POST":
        #do this incase of a GET request:
        return redirect("monster-list")
    #read the servants name the user typed then look it up in the database:
    query_name = requests.POST.get("query_name","").strip()
    #if the user didnt type anything show a message error:
    if not query_name:
        messages.error(request,"please enter a monster")
        #send them back to the list:
        return redirect("monster-list")
    #if its a post request send it to the API:
    
    


        
    