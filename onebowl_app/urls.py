from django.urls import path
from .views import RecipeListCreateView,RecipeDetailView, IngredientListCreateView

urlpatterns = [
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-details'),
    path('ingredients/', IngredientListCreateView.as_view(), name='recipe-ingredient')
]