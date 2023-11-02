from django.urls import path
from . import views

urlpatterns = [
    path('', views.Menu.as_view(), name="Home"),
    path('meal/<int:pk>/', views.MenuItemDetails.as_view(), name="menu_item"),
]
