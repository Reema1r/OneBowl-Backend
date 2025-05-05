from django.urls import path
from .views import RecipeListCreateView,RecipeDetailView, IngredientListCreateView,ShoppingListCreateList, ShoppingListDetailView,IngredienDeleteView


urlpatterns = [
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-details'),
    path('ingredients/', IngredientListCreateView.as_view(), name='recipe-ingredient'),
    path('ingredients/<int:pk>/', IngredienDeleteView.as_view(), name='ingredient-delete'),
    path('shoppinglist/', ShoppingListCreateList.as_view(), name='recipe-shopping-list'),
    path('shoppinglist/<int:pk>/', ShoppingListDetailView.as_view(), name='shopping-list-details')

]