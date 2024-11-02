from django.db import models
from users.models import Profile , Location
import uuid
from .consts import CARS_BRANDS , TRANSMISSION_OPTIONS
from .utils import user_listing_path
# used for givving a random values 

# Create your models here.

# for implementing a model we can bypassing the default values 
# by assigning it by our selves choosing the option 1 then assigning it to ('')   

class Listing(models.Model):
    id = models.UUIDField(primary_key= True , unique= True , 
                        default= uuid.uuid4 , editable= False)
    # this uuidfield is used for uninque fields and has a lot of advantages 
    # specially used for id 
    created_at = models.DateTimeField(auto_now_add= True)
    # to save the time only when the model is created (added)
    updated_at = models.DateTimeField(auto_now = True)
    # to save the time when we update the model 
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE )
    brand = models.CharField(max_length=24, choices=CARS_BRANDS, default=None)
    # this to make an insedered list to choose a brand
    model = models.CharField(max_length=64)
    vin = models.CharField(max_length=17)
    mileage = models.IntegerField(default=0)
    color = models.CharField(max_length=24)
    description = models.TextField()
    engine = models.CharField(max_length=24)
    transmission = models.CharField(
        max_length=24, choices=TRANSMISSION_OPTIONS, default=None)
    # this to make an insedered list to choose a transmission 
    location = models.OneToOneField(
        Location, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=user_listing_path)

    def __str__(self) :
        return f'{self.seller.user}\'s Listing - {self.model}'
    
class LikedListing(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE)
    like_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.listing.model} listing liked by {self.profile.user.username}'
