from django.db import models

# Create your models here.
#what do i want to store for each monster?:
class Monster(models.Model):
    #every monster name must be unique:
    name = models.CharField(unique=True, max_length=50)
    #what type the monster is (brute wyvern,eldar dragon,flying wyvern etc):
    type = models.CharField(max_length=100,null=True,blank=True)
    #display the type of element it will use
    element = models.CharField(max_length=100,null=True,blank=True)
    #add a small description for each monster explaining their biography:
    description = models.CharField(max_length=500,null=True,blank=True)
    #add an image for each monster:
    image_url = models.URLField()
    #make django show me the name when printing the monster:
    def __str__(self):
        return self.name
    

