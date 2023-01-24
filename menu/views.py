from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import FoodItem, DrinkItem


def menus(request):
    return render(request, "menus_page.html")


class FoodMenu(generic.ListView):

    model = FoodItem
    template_name = "food_menu.html"
    context_object_name = "food_items"

    def get_queryset(self):
        queryset = {
            "dinner_items": FoodItem.objects.all().filter(
                on_menu=True, food_menu_section=0
            ),
            "desserts_items": FoodItem.objects.all().filter(
                on_menu=True, food_menu_section=1
            ),
        }
        return queryset
