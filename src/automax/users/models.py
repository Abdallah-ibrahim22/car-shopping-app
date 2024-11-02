from django.db import models
from django.contrib.auth.models import User
# to import the user model (it's a built in model )
from .utils import user_directory_path

# installing django-localflavor then we assign it on the installation apps in the settings
from localflavor.us.models import USStateField , USZipCodeField
# then we import our wanted fields

# Create your models here.

class Location(models.Model):
    address_1 = models.CharField(max_length=125 , blank=True)
    address_2 = models.CharField(max_length=125 , blank=True)
    city = models.CharField(max_length=50)
    state = USStateField(default='NY')
    zip_code = USZipCodeField(blank=True)

    def __str__(self) -> str:
        return f'Location : {self.id-5}'



class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    photo = models.ImageField( upload_to= user_directory_path ,null=True)
    bio = models.CharField(max_length=140 , blank=True)
    number = models.CharField(max_length=12 , blank=True)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL , null=True)
    # we say if the location is deleted the profile will stand with location (NULL)

    def __str__(self) : 
        return f'{self.user}\'s profile : {self.user.id-4}'