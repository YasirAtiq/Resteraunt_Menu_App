from django.shortcuts import render
from django.views import generic
from .models import Meal, MEAL_TYPE

class Menu(generic.ListView):
    template_name = "index.html"
    model = Meal

    def get_queryset(self):
        return Meal.objects.order_by('meal')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meals = []

        for category, category_name in MEAL_TYPE:
            meals.append((category_name, Meal.objects.filter(category=category)))

        context["meals"] = meals
        return context
