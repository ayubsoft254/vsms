from django.db import models

# Create your models here.
class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    VIN = models.CharField(max_length=17, unique=True)
    year = models.IntegerField()
    specs = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.IntegerField()
    color = models.CharField(max_length=50)
    photos = models.ImageField(upload_to='vehicles/photos/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('sold', 'Sold'), ('reserved', 'Reserved')])

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"    