from django.db import models

# Create your models here.

class Airport(models.Model) : 
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=20)

    def __str__(self) : 
        return f"({self.code}) {self.city}"
class Flight(models.Model) : 
    origin = models.ForeignKey(Airport, related_name=("departures"), on_delete=models.CASCADE)
    destination = models.ForeignKey(Airport, related_name=("arrivals"), on_delete=models.CASCADE)
    duration = models.IntegerField()

    def __str__(self)  :
        return f"{self.origin} to {self.destination}"
    
class passenger(models.Model) : 
    name = models.CharField(max_length=10)
    surname =models.CharField(max_length=100)
    flights = models.ManyToManyField(Flight,related_name="passengers") 
    def __str__(self) : 
        return f"{self.name} {self.surname}"


