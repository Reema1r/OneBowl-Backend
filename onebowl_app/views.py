# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recipe, Ingredient, ShoppingList
from .serializers import RecipeSerializer,IngredientSerializer, ShoppingListSerializer
from django.shortcuts import get_object_or_404


from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.password_validation import validate_password
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


# Recipe views
class RecipeListCreateView(APIView):
    permission_classes = [IsAuthenticated]  
    
    def get(self, request):
        recipes = Recipe.objects.filter(owner=request.user)
        serializer=RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=200)
    
    def post(self,request):
        serializer=RecipeSerializer(data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
            
        return Response(serializer.errors,status=400)
    
    
class RecipeDetailView(APIView): 
    permission_classes = [IsAuthenticated]  

    def get_object(self,pk,user):
        recipe= get_object_or_404(Recipe,pk=pk)
        if recipe.owner != user:
                raise PermissionDenied("Access denied. You are not allowed to access this recipe.")
        return recipe
        
    def get(self,request,pk):
        recipe=self.get_object(pk,request.user) 
        serializer =RecipeSerializer(recipe)
        return Response(serializer.data, status=200)
    
    def patch(self,request,pk):
        recipe=self.get_object(pk,request.user)
        serializer =RecipeSerializer(recipe, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def delete(self,request,pk):
        recipe=self.get_object(pk,request.user)
        recipe.delete()
        return Response (status=204) 
        
        
        
# Ingredient views
class IngredientListCreateView(APIView):
    permission_classes = [IsAuthenticated]  

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
    
    
class IngredienDeleteView(APIView):
    permission_classes = [IsAuthenticated]  

    def get_object(self,pk):
        return get_object_or_404(Ingredient,pk=pk)
    
    def get(self,request,pk):
        ingredient=self.get_object(pk) 
        serializer =IngredientSerializer(ingredient)
        return Response(serializer.data, status=200)
    
    def delete(self,request,pk):
        ingredient=self.get_object(pk)
        ingredient.delete()
        return Response (status=204) 
    
# Shopping list views
class ShoppingListCreateList(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self,request):
        shopping_lists = ShoppingList.objects.filter(owner=request.user)
        serializer=ShoppingListSerializer(shopping_lists, many=True)
        return Response(serializer.data, status=200)
    
    def post(self,request):
        serializer=ShoppingListSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
            
        return Response(serializer.errors,status=400)
    
    
class ShoppingListDetailView(APIView):
    permission_classes = [IsAuthenticated]  

    def get_object(self,pk,user):
        shopping_list= get_object_or_404(ShoppingList,pk=pk)
        if shopping_list.owner != user:
            raise PermissionDenied("Access denied. You are not allowed to access this shopping list.")
        return shopping_list
    
    def get(self,request,pk):
        shopping_list=self.get_object(pk,request.user) 
        serializer =ShoppingListSerializer(shopping_list)
        return Response(serializer.data, status=200)
    
    def patch(self,request,pk):
        shopping_list=self.get_object(pk,request.user)
        serializer =ShoppingListSerializer(shopping_list, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def delete(self,request,pk):
        shopping_list=self.get_object(pk,request.user)
        shopping_list.delete()
        return Response (status=204) 
    
# Sign up view
class SignUpView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            validate_password(password)
        except ValidationError as error:
            return Response({'error': error.messages}, status=400)

        # create user 
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # create an access and refresh token
        tokens = RefreshToken.for_user(user)
        return Response(
            {
                'refresh': str(tokens),
                'access': str(tokens.access_token)
            },
            status=201
        )