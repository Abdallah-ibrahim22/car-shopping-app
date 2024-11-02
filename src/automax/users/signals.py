from django.contrib.auth.models import User
# importing the user obj
from django.db.models.signals import post_save , post_delete
# here importing the (post_save & ....) signals that inform us about something happening
from django.dispatch import receiver
# importing the reciever used to check if something happend do the method below
from .models import Profile , Location

@receiver(post_save , sender = User)
# here we first check if the sender obj (User) is saved (post_save) do the method below
def create_user_profile(sender , instance , created , **kwargs):
    # the function recieves a instance (user that we created)
    # & the created bool to inform us that the user is created
    if created :
        Profile.objects.create(user = instance)

@receiver(post_save , sender = Profile)
def create_profile_location(sender , instance : Profile , created , **kwargs):
    if created :
        profile_location = Location.objects.create()
        # creating an empty obj with type location so we can link it with the new profile
        instance.location = profile_location
        # we assign the new empty location to the profile then we save it
        instance.save() 

@receiver(post_delete , sender = Profile)
def create_profile_location(sender , instance : Profile , *args , **kwargs):
    if instance.location :
        instance.location.delete()
    # so here we tell if the (profile) model is deleted and the sended 
    # instance (profile) has a location => we delete it's location  