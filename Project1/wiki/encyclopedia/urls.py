from django.urls import path

from . import views


urlpatterns = [
    
    path("wiki/", views.index, name="index"),
    path("wiki/<str:entry>",views.show_entry,name="entry"),
    path("new_page/",views.new_page , name="new"),
    path("error/",views.show_error,name="error"),
    path("edit/<str:entry>",views.edit,name="edit"),
    path("random/",views.random_entry,name="random")

]
