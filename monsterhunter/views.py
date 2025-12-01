from django.shortcuts import render,redirect,get_object_or_404
#import the model:
from .models import Monster,Item,MonsterItemDrop,Element
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

# Define the API endpoint for monster data
imported_monster = "https://mhw-db.com/monsters"

def import_monster(request):
    # Check if the request method is not POST
    if request.method != "POST":
        # Redirect to monster list if not a POST request
        return redirect("monster-list")
    
    # Get and clean the search query from the form
    query_name = request.POST.get("query_name", "").strip()
    
    # Check if the query is empty
    if not query_name:
        messages.error(request, "Please enter a monster name")
        return redirect("monster-list")
    
    try:
        # Make an HTTP GET request to the MHW API
        resp = requests.get(imported_monster, timeout=20)
        # Raise an exception for HTTP errors (4xx, 5xx)
        resp.raise_for_status()
        # Parse the JSON response
        data = resp.json()
        print("\n=== DEBUG: First 3 Monsters ===")
        for monster in data[:3]:  # Show first 3 monsters
            print(f"- {monster.get('name')} ({monster.get('species')})")
        print(f"\nSearching for: '{query_name}'")
        print("\n=== DEBUG: Data Type ===")
        print(f"Type of 'data': {type(data)}")
        print(f"Number of monsters in response: {len(data)}")
        # Initialize variables for monster matching
        match = None
        # Convert search query to lowercase for case-insensitive comparison
        q_lower = query_name.lower()
        
        # Search through the list of monsters
        for m in data:
            # Get the monster's name
            name = m.get("name")
            # Skip if no name is found
            if not name:
                continue
            # Check if the search term is in the monster's name
            if q_lower in name.lower():
                match = m
                break
        
        # If no match found, show error and redirect
        if match is None:
            messages.error(request, f"No match found for {query_name}. Try a more exact name :)")
            return redirect("monster-list")
        
        # Extract monster data from the match
        name = match.get("name")
        species = match.get("species")
        elements = match.get("elements")
        description = match.get("description")
        
        # Create or update the monster in the database
        obj, created = Monster.objects.update_or_create(
            name=name,
            defaults={
                "species": species,
                "elements": elements,
                "description": description,
            }
        )
        #extract item data from the match:
        #create or update the items in the database:
        item_obj,created = Item.object.update_or+create(
            name=name
            "description":item_description
            "rarity":item_rarity,
            "value":item_value
        )
        # Show success message
        messages.success(request, f"Successfully imported {name}!")
        
        # Debug information (visible in server console)
        # print("API Response:", data)
        # print("Searching for:", query_name)
        
    # Handle HTTP errors (4xx, 5xx)
    except requests.exceptions.HTTPError as http_err:
        error_msg = f"HTTP error: {http_err}. Response: {resp.text[:200]}"
        messages.error(request, "Failed to fetch monster data. Please try again.")
        print(error_msg)
        
    # Handle connection errors, timeouts, etc.
    except requests.exceptions.RequestException as req_err:
        error_msg = f"Request failed: {req_err}"
        messages.error(request, "Could not connect to the server. Please check your connection.")
        print(error_msg)
        
    # Handle JSON parsing errors
    except ValueError as json_err:
        error_msg = f"Failed to parse JSON: {json_err}. Response: {resp.text[:200]}"
        messages.error(request, "Invalid response from the server. Please try again.")
        print(error_msg)
        
    # Catch any other unexpected errors
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        messages.error(request, "An unexpected error occurred.")
        print(error_msg)

    # Always redirect back to the monster list
    return redirect("monster-list")
        
        
        
    
    
    


        
    