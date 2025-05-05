from django.urls import path
from .views import RecipeListCreateView,RecipeDetailView, IngredientListCreateView,ShoppingListCreateList, ShoppingListDetailView,IngredienDeleteView,CreateUserView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='sign-up'),
    path('token/', TokenObtainPairView.as_view(), name='get-token'),
    path('token/refresh', TokenRefreshView.as_view(), name='refresh-token'),
    
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-details'),
    path('ingredients/', IngredientListCreateView.as_view(), name='recipe-ingredient'),
    path('ingredients/<int:pk>/', IngredienDeleteView.as_view(), name='ingredient-delete'),
    path('shoppinglist/', ShoppingListCreateList.as_view(), name='recipe-shopping-list'),
    path('shoppinglist/<int:pk>/', ShoppingListDetailView.as_view(), name='shopping-list-details')

]