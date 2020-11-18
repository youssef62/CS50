from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("Add" , views.add , name = "add") , 
    path("Listing/<int:id>",views.show_listing,name="listing"),
    path("watchlist/",views.watch_list,name="watchlist"),
    path("categories/",views.category_list,name="categories"),
    path("categories/<int:id>", views.show_by_category,name="show_by_category"),
    path("auctions_won/",views.auction_won,name="won")
]
