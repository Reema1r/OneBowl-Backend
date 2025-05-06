from django.db import models
from django.contrib.auth.models import User

# Recipe model
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    instructions = models.TextField()
    img_url = models.CharField(max_length=1000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')

    def __str__(self):
        return self.name 
    
# Ingredient model
class Ingredient(models.Model):
    name=models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE , related_name="ingredients")
    
    def __str__(self):
        return self.name
    
    
# Shopping list model
class ShoppingList(models.Model):
    name=models.CharField(max_length=100)
    ingredients_list=models.TextField() 
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shopping_lists') 

    
    def __str__(self):
        return self.name

    
    
    

