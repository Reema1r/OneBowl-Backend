from rest_framework import serializers
from .models import Recipe, Ingredient, ShoppingList

from django.contrib.auth.models import User

# User serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']  )
        return user



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
    user = serializers.PrimaryKeyRelatedField(read_only=True)  

    class Meta:
        model=Recipe
        fields=['id', 'name', 'description', 'instructions', 'img_url', 'ingredients','user']
        
        
        
# Shopping List serializer  
class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model=ShoppingList
        fields="__all__"