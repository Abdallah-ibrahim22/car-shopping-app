from django.shortcuts import redirect, render , get_object_or_404
from django.http import HttpRequest ,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Listing , LikedListing
from .forms import ListingForm
from users.forms import LocationForm
from django.contrib import messages 
from main.filters import ListingFilter


# Create your views here.

def landing_view(request : HttpRequest):
    return render(request , 'views/main.html')

# this will redirect me auto to the login url if i wasn't loggedin
@login_required(login_url='login')
def home_view(request : HttpRequest):
    listings = Listing.objects.all()
    listing_filter = ListingFilter(request.GET ,queryset= listings)
    # so we send the (request.GET) to get the data submitted then 
    # we filter it from the whole listing objs 
    user_liked_listing = LikedListing.objects.filter(
        profile = request.user.profile 
    ).values_list('listing')
    # so fn (values_list) : means to return the column that it's name passed to this fn
    liked_listing_ids = [listing_id for listing_id in user_liked_listing]
    # here we make a list that contains the ids for each liked list
    context = {
        'liked_listing_ids' : liked_listing_ids ,
        'listing_filter' : listing_filter,
    }
    return render(request , 'views/home.html' , context)

def list_view(request : HttpRequest):
    if request.POST :
        try :
            listing_form = ListingForm(request.POST , request.FILES) 
            # to make the form contain the info in the request (data & media files)
            location_form = LocationForm(request.POST) 
            if listing_form.is_valid() and location_form.is_valid() :
                listing = listing_form.save(commit=False)
                # this means that the form will be saved in the listing var 
                # untill we assign the other unsubmitted field
                # so now the listing var is a model with listing type
                listing_location = location_form.save()
                # so here listing_location is a model with type location
                listing.seller = request.user.profile
                listing.location = listing_location
                listing.save()
                messages.info(
                    request , f'{listing.model} Listing Posted Successfully !'
                )
                return redirect('home')
            else :
                raise Exception()
        except Exception as e :
            print(e)
            messages.error(request , 'Error occured while posting the list .')
            

    else :
        listing_form = ListingForm() 
        location_form = LocationForm() 
    
    return render(request,'views/list.html' , {
        'listing_form' : listing_form , 
        'location_form' : location_form ,
    })

@login_required
def listing_view(request : HttpRequest , id):
    try:
        linsting = Listing.objects.get(id=id)
        if linsting is None :
            raise Exception
        return render(request , 'views/listing.html' , {
            'listing' : linsting ,
        })
    except Exception as e:
        messages.error(request, f'Invalid UID {id} was provided for the listing')
        return redirect('home')
    

@login_required
def edit_view(request : HttpRequest , id):
    try : 
        listing = Listing.objects.get(id = id)
        if listing is None : 
            raise Exception
        if request.POST :
            listing_form = ListingForm( request.POST , 
                            request.FILES ,instance=listing)
            location_form = LocationForm( request.POST , instance=listing.location)
            # (instance) used to make the form assigned with the values of the model 
            # that we pass to it
            if listing_form.is_valid() and location_form.is_valid() : 
                listing_form.save()
                location_form.save()
                messages.success(request , f'Listnig {id} updated successfully !')
                return redirect('home')
            else : 
                raise Exception 
        else : 
            listing_form = ListingForm(instance=listing)
            location_form = LocationForm(instance=listing.location)
        context = {
            'listing' : listing ,
            'listing_form' : listing_form ,
            'location_form' : location_form ,
        }
        return render(request , 'views/edit.html' , context)
    except Exception as e : 
        messages.error(request , 
                    f'An Error occurred while trying to update the Listing !')
        return redirect('home')

@login_required 
def like_wiew(request : HttpRequest , id):
    listing = get_object_or_404(Listing , id = id)
    # (get_object_or_404) it gives us an obj that have a particular id or returns 404_error

    liked_listing , created = LikedListing.objects.get_or_create(
        profile = request.user.profile , listing = listing
    )
    # (get_or_create) this fn gives us to var 
    # the first : obj contains (these passed values : profile , listing)
    # the second one : boolean that informs us if this obj created or already exist

    if not created :
        liked_listing.delete()
    else :
        liked_listing.save()
    
    # here to toggle if the used liked or unliked the post

    return JsonResponse({
        'is_liked_by_user' : created ,
    })