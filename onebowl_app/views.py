from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer

# Create your views here.
class RecipeListCreateView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer=RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=200)