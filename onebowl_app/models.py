from django.db import models

# Create your models here.

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    instructions = models.TextField()
    image_url = models.CharField(max_length=255)
    
    def __str__(self):
        return self.recipe_name 
    
    

