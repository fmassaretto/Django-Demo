from django.shortcuts import render
from .models import Food

# Create your views here.

def food_list(request):
    foods = Food.objects.all()
    print(foods)
    
    return render(request, 'foodlog/index.html', {'foods': foods})
