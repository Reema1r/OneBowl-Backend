from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    instructions = models.TextField()
    img_url = models.CharField(max_length=400)
    
    def __str__(self):
        return self.name 
    
    
class Ingredient(models.Model):
    name=models.CharField(max_length=50)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE , related_name="ingredients")
    
    def __str__(self):
        return self.name
    
    
class ShoppingList(models.Model):
    name=models.CharField(max_length=50)
    ingredients_list=models.TextField() 
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    
    
    

