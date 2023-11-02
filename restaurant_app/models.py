from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("dessert", "Dessert")
)
STATUS = (
    (1, "Available"),
    (0, "Unavailable")
)



class Meal(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    ingredients = models.CharField(max_length=4000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=200, choices=MEAL_TYPE)
    cook = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal
