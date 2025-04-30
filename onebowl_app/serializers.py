from rest_framework import serializers
from .models import Recipe

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields="__all__"