from django.contrib import admin
from .models import Meal


class MealItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status")
    list_filter = ("status", )
    search_fields = ("meal", "ingredients")

admin.site.register(Meal, MealItemAdmin)