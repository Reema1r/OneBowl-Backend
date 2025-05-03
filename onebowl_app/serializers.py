from rest_framework import serializers
from .models import Recipe, Ingredient, ShoppingList


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ingredient
        fields="__all__"
        
        
# Django REST framework :https://www.django-rest-framework.org/api-guide/relations/
# Stackoverflow: https://stackoverflow.com/questions/51182823/django-rest-framework-nested-serializers
class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    class Meta:
        model=Recipe
        fields=['id', 'name', 'description', 'instructions', 'img_url', 'ingredients']
        
        
class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model=ShoppingList
        fields="__all__"