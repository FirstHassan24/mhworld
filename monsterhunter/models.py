from django.db import models

# Create your models here.
#what do i want to store for each monster?:
class Monster(models.Model):
    #every monster name must be unique:
    name = models.CharField(unique=True, max_length=50)
    #what type the monster is (brute wyvern,eldar dragon,flying wyvern etc):
    species = models.CharField(max_length=100,null=True,blank=True)
    #display the type of element it will use
    elements = models.CharField(max_length=100,null=True,blank=True)
    #add a small description for each monster explaining their biography:
    description = models.CharField(max_length=500,null=True,blank=True)
    #add an image for each monster:
    image_url = models.URLField(null=True,blank=True)
    #make django show me the name when printing the monster:
    def __str__(self):
        return self.name
#TODO: make elements into a seperate table and make an association:
class Element(models.Model):
    name = models.CharField(unique=True)
    description = models.TextField(max_length=300,null=True,blank=True)

    
#create an item table:
class Item(models.Model):
    #what fields do i need from items?
    name = models.CharField(unique=True,max_length=50)
    description = models.TextField(null=True,blank=True)
    rarity = models.IntegerField()
    value = models.IntegerField()  
    #shows me the name of the table when i print it:
    def __str__(self):
        return self.name 

#create a many to many relationship between monster and item:
class MonsterItemDrop(models.Model):
    #which monster is this drop for?
    monster = models.ForeignKey(Monster,on_delete=models.CASCADE)
    #which item does it drop?:
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    #how is it obtained?
    #TODO make a choice field so the user can only choose between carving and capture
    method = models.CharField(max_length=100)
    #what are the drop chance:
    chance = models.IntegerField()
    

#TODO: add a text field for item, make it so the user can type whatever add it to a list of items,find the ones that existes and then associate them and create the ones that dont exist and asscociate them.
#TODO:make it so when the user types it shows them autocomplete of whats in the api, 
