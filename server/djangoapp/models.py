from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Other fields as needed

    def __str__(self):
        return self.name  # This makes it print the name instead of "Object (1)"


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    # Many-to-One relationship
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE) 
    dealer_id = models.IntegerField() # Refers to a dealer created in your Node.js backend
    name = models.CharField(max_length=100)
    
    # Choices for the type of car
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('SPORTS', 'Sports Car')
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    
    # Year with validation rules
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2024),
            MinValueValidator(2015)
        ])

    def __str__(self):
        return self.name