from django.db import models

# Create your models here.
class Food(models.Model):
    meal_type = models.CharField(max_length=100)
    calories = models.DecimalField(max_digits=10, decimal_places=0)
    proteins = models.DecimalField(max_digits=10, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=10, decimal_places=2)
    fats = models.DecimalField(max_digits=10, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
