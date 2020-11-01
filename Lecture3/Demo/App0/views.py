from django.shortcuts import render
import datetime 
from django.http import HttpResponse 

# Create your views here.


def question( request ) :   
    now = datetime.datetime.now()
    time = now.hour   
    
    return render(request ,"App0/index.html",{
        "time": time <= 12 
    }) 



 