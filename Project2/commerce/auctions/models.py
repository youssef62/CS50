from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass 

class Bid(models.Model) : 
    price = models.FloatField(null=True)
    bidder = models.ForeignKey(
        User, related_name="bids", null = True , on_delete=models.CASCADE)

class Category(models.Model) : 
    name = models.CharField( max_length=50)
    
    def __str__(self) : 
        return self.name

class Comment (models.Model):
    user = models.ForeignKey(User, null= True , related_name="comments_posted" , on_delete = models.CASCADE)
    content = models.CharField(max_length=500)

class Listing(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    current_bid = models.OneToOneField(Bid,null=True,related_name="list", on_delete=models.CASCADE)
    photo = models.CharField(null=True, max_length=100)
    comments = models.ManyToManyField(Comment, related_name="listings_commented")
    creation_date = models.CharField(null=True,max_length=20)
    creator = models.ForeignKey(User , null=True, related_name="listing", on_delete=models.CASCADE)
    watch_listed_by = models.ManyToManyField(User, "watch_list")
    category = models.ForeignKey(Category, null=True , related_name=("list"), on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True )
