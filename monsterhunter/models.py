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
    image_url = models.URLField()
    #make django show me the name when printing the monster:
    def __str__(self):
        return self.name
    
#creating a table for things  my monster can drop:
class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    rarity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} (⭐{self.rarity})"

#creating a table for the relationship between monster and item:
class MonsterItemDrop(models.Model):
    monster = models.ForeignKey(
        Monster,
        on_delete=models.CASCADE,
        related_name="drops",       # monster.drops.all()
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name="dropped_by",  # item.dropped_by.all()
    )

    method = models.CharField(
        max_length=50,
        help_text="carve, capture, quest reward, etc.",
    )
    rank = models.CharField(
        max_length=20,
        blank=True,
        help_text="low, high, master",
    )
    chance = models.IntegerField(
        help_text="Drop chance percentage (e.g. 34 for 34%)",
    )

    def __str__(self):
        return f"{self.monster} → {self.item} ({self.method}, {self.chance}%)"

    

