from django.contrib import admin
from .models import Food

class FoodAdmin(admin.ModelAdmin):
    lista = ('meal type', 'calories', 'proteins')
admin.site.register(Food)

# Register your models here.
