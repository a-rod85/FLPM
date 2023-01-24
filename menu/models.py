from django.db import models

FOOD_MENU_SECTION = ((0, "Dinner"), (1,"Desserts"),(2, "New Item"))
DRINKS_MENU_SECTION = (
    (0, "Cocktails/Beers"), 
    (1,"White Wine"),
    (2, "Red Wine"), 
    (3,"Champagne"),
    )

class FoodItem(models.Model):

    dish_id = models.AutoField(primary_key=True)
    dish_name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    food_menu_section = models.IntegerField(choices=FOOD_MENU_SECTION, default=2)
    on_menu = models.BooleanField(default=False)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ["-on_menu"]

    def __str__(self:)
        return self.dish_name


class DrinkItem(models.Model):

    drink_id = models.AutoField(primary_key=True)
    drink_name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=150, unique=True)
    price = models.FloatField()
    drinks_menu_section = models.IntegerField(choice=DRINKS_MENU_SECTION, default=3)
    on_menu = models.BooleanField(default=False)
    updated_on = models.DataTimeField(auto_now=True)
    
    class Meta:
        ordering = ["on_menu"]

    def __str__(self):
        return self.drink_menu
