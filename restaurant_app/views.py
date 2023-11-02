from django.shortcuts import render
from django.views import generic
from .models import Meal


class Menu(generic.ListView):
    queryset = Meal.objects.order_by("meal")
    template_name = "index.html"


class MenuItem(generic.DetailView):
    model = Meal
    template_name = "meal_view_detail.html"
