# Uncomment the following imports before adding the Model code

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name  # Devuelve el nombre de la marca


# Modelo para el Modelo del Auto
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Relación de Muchos a Uno
    dealer_id = models.IntegerField()  # ID que se referirá al concesionario en Mongo
    name = models.CharField(max_length=100)
    
    # Opciones limitadas para el tipo de auto
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    
    # Validador de años
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])

    def __str__(self):
        # Devuelve la marca y el modelo juntos (Ej. "Toyota Corolla")
        return f"{self.car_make.name} {self.name}"
