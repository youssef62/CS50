from django.shortcuts import render
from FlightApp.models import *
# Create your views here.
from django.http import HttpResponse

def index (request) : 
    
    return render(request,"FlightApp/Flights.html",{    
        "Flights" : Flight.objects.all() 
    })


def flight ( request , flight ) : 
    if Flight.objects.filter(id=flight).exists() :  
        f = Flight.objects.get(id=flight)
        return render(request,"FlightApp/flight.html" , {
            "flight" : f  , 
            "passengers" : f.passengers.all()
        })
    else : 
        return HttpResponse("<h1> This flight number does not exist ! </h1>")
