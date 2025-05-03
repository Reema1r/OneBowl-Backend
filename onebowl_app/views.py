# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recipe, Ingredient
from .serializers import RecipeSerializer,IngredientSerializer

from django.shortcuts import get_object_or_404

# Recipe views
class RecipeListCreateView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer=RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=200)
    
    def post(self,request):
        serializer=RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
            
        return Response(serializer.errors,status=400)
    
    
class RecipeDetailView(APIView):    
    def get_object(self,pk):
        return get_object_or_404(Recipe,pk=pk)
    
    def get(self,request,pk):
        recipe=self.get_object(pk) 
        serializer =RecipeSerializer(recipe)
        return Response(serializer.data, status=200)
    
    def patch(self,request,pk):
        recipe=self.get_object(pk)
        serializer =RecipeSerializer(recipe, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def delete(self,request,pk):
        recipe=self.get_object(pk)
        recipe.delete()
        return Response (status=204) 
        
        
        
# Ingredient views
class IngredientListCreateView(APIView):
    def get(self, request):
        ingredients = Ingredient.objects.all()
        serializer=IngredientSerializer(ingredients, many=True)
        return Response(serializer.data, status=200)
    
    def post(self,request):
        serializer=IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
            
        return Response(serializer.errors,status=400)
    