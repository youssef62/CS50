from django.urls import path 
from . import views 


urlpatterns = [
    path("" ,views.index, name ="task") ,
    path("add/" , views.add , name = "add")
]
