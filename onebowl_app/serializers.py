from rest_framework import serializers
from .models import Recipe, Ingredient, ShoppingList


# Ingredient serializer
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ingredient
        fields="__all__"
        
        
# Recipe serializer
# Django REST framework :https://www.django-rest-framework.org/api-guide/relations/
# Stackoverflow: https://stackoverflow.com/questions/51182823/django-rest-framework-nested-serializers
class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model=Recipe
        fields=['id', 'name', 'description', 'instructions', 'img_url', 'ingredients']
        read_only_fields = ['id', 'owner']
        
    def create(self, validated_data):
        user = self.context['request'].user 
        return Recipe.objects.create(owner=user, **validated_data)

# Shopping List serializer  
class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model=ShoppingList
        fields="__all__"
        read_only_fields = ['id', 'owner']

    def create(self, validated_data):
        user = self.context['request'].user 
        return ShoppingList.objects.create(owner=user, **validated_data)
