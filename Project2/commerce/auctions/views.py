from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from auctions.forms import *
from .models import *
from datetime import date

def add_to_watchlist(listing_id , user ) : 
    listing = Listing.objects.get(pk=listing_id)
    user.watch_list.add(listing)
        
def remove(lisitng_id , user ) : 
    listing = Listing.objects.get( pk = lisitng_id) 
    user.watch_list.remove(listing)


def index(request):
    if request.method =="POST" : 
        id = request.POST["item"] 
        listing = Listing.objects.get(pk=id)
        watchlist = request.user.watch_list.filter(is_active=True)
        if listing in watchlist:
            remove(id, request.user)
        else:
            add_to_watchlist(id, request.user)
        
    return render(request, "auctions/index.html" , {
        "title" : "Active Listings",
        "Listings" : Listing.objects.filter(is_active=True)
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def add(request) : 

    if request.method == "POST" : 
        returned_form =ListingForm(request.POST) 
        
        if returned_form.is_valid():

            current_b = Bid(price=returned_form.cleaned_data["min_bid"])
            current_b.save()
            l = Listing(title = returned_form.cleaned_data["title"],
            description = returned_form.cleaned_data["description"],
            photo = returned_form.cleaned_data["photo"],
            creation_date=date.today().strftime("%B %d, %Y"),
            creator=request.user, 
            current_bid=current_b
            )
            
            l.save()
            return HttpResponseRedirect(reverse("index"))
        else :
            return render(request,"auctions/add.html",{
                "form": returned_form
            })
    return render(request,"auctions/add.html" , {
        "form" : ListingForm() 
    })


def show_listing(request,id) :
    message =""
    listing = Listing.objects.get(pk=id)
    if request.method == "POST" :
        bid = listing.current_bid
        
        if request.POST.get("comment_submit") : 
            content = request.POST["content"]
            comment = Comment(user = request.user , content = content )
            comment.save()
            listing.comments.add(comment)
        elif request.POST.get("bid_submit"):
            price = request.POST["price"] 
            
            if request.user == listing.creator  : 
                message = " You can't bid on your own listing."
            elif bid.price == int(price) and bid.bidder != None :
                message = "You should bid higher than current bid"
            else :   
                bid.price = price
                bid.bidder = (request.user)
                bid.save()
        
        elif request.POST.get("edit_watchlist") : 
            watchlist = request.user.watch_list.filter(is_active=True)
            if listing in watchlist : 
                remove(id,request.user)
            else : 
                add_to_watchlist(id,request.user)
        elif request.POST.get("end_auction") : 
            listing.is_active = False 
            listing.save()
            
    if request.user.is_authenticated:
        watchlist = request.user.watch_list.filter(is_active=True)
    else:
        watchlist = []
    return render(request,"auctions/listing.html",{
        "listing" : listing , 
        "watch_list" :watchlist,
        "message" : message,
        "comments" : listing.comments.all()
    })



def watch_list(request)  :
    if request.method == "POST" : 
        remove(request.POST["item"] , request.user )
        
    return render(request,"auctions/index.html  ",{
        "title" : 'Watch list : ' , 
        "Listings" : request.user.watch_list.filter(is_active=True)
    })


def category_list(request) : 
    return render ( request , "auctions/categories.html" , 
    {
        "categories" : Category.objects.all()
    })


def show_by_category(request , id ) :
    category = Category.objects.get(pk=id) 
    print( Listing.objects.filter(category=category) )
    return render ( request , "auctions/index.html" , {
        "title" : category , 
        "Listings" : Listing.objects.filter(category=category).filter(is_active=True)
    })


def auction_won(request) : 
    return render(request , "auctions/index.html" , {
        "title" : "Auctions Won " , 
        "Listings" : Listing.objects.filter(is_active=False).filter(current_bid__bidder=request.user)
    })