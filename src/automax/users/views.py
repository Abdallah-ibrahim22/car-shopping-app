from django.shortcuts import render
from django.http import HttpRequest 
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate , login , logout
# to help us for making forms to the users model 
from django.contrib import messages 
from django.views import View 
# used to make a classes based view 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# this used to decorate the classes
from users.forms import ProfileForm , UserForm , LocationForm
from main.models import Listing , LikedListing

# Create your views here.

def login_view(request : HttpRequest) :
    login_form = AuthenticationForm()
    if request.method == 'POST' :
        login_form = AuthenticationForm(request=request , data = request.POST)
        # giving the data to the form then checking if the form has a right data 
        # we get the username and the password from the form then
        # we assign these values to the uathentication obj to make a new user obj
        if login_form.is_valid() :
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            # this (authenticate) is used to see if the input data that 
            # submitted on the form matches the data for any user that saved in the db
            if user is not None :
                login(request , user)
                messages.success(request , f'You r logged in with {username}')
                # here we make a success message after loggingin 
                return redirect('home')
        else : 
            messages.error(request , f'Error accured during loggingin !!')

    context ={ 'login_form' : login_form}
    return render(request , 'views/login.html' , context)




class RegisterView(View):
    # means do this incase the request is get
    def get(self,request:HttpRequest):
        register_form = UserCreationForm()
        context = { 'register_form' :  register_form}

        return render(request , 'views/register.html' , context ) 
    def post(self , request : HttpRequest):
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid() :
            user = register_form.save()
            # here we tell the db to save this form model so it will create new user
            user.refresh_from_db()
            # this to refresh the content of db with the data in the form
            login(request , user)
            messages.success(request , f'User {user.username} registered successfully')
            return redirect('home')
        else :
            context = { 'register_form' :  register_form}
            messages.error(request , f'Error accured during loggingin !!')
            return render(request , 'views/register.html' , context ) 


# to tell that if u rn't loggedin u will not logout 
@login_required(login_url='login')
def logout_view(request : HttpRequest):
    logout(request)
    return redirect('main')

@method_decorator(login_required, name='dispatch')
# this means we can't reach any methods in this class without loggingin 
# and we send this decorator to the a method in the (View) class 
# to check for that
class Profile_view(View):
    def get(self , request:HttpRequest):
        user_listings = Listing.objects.filter(seller = request.user.profile)
        # so now we get the listing that related to the loggedin user
        profile_form = ProfileForm(instance=request.user.profile)
        user_form = UserForm(instance=request.user)
        location_form = LocationForm(instance=request.user.profile.location)
        user_liked_listings = LikedListing.objects.filter(profile = request.user.profile)
        context = {
            'profile_form' : profile_form  , 
            'user_form' : user_form , 
            'location_form' : location_form , 
            'user_listings' : user_listings ,
            'user_liked_listings' : user_liked_listings ,
        }
        return render(request , 'views/profile.html' , context)
    def post(self , request:HttpRequest):
        user_listings = Listing.objects.filter(seller = request.user.profile)
        profile_form = ProfileForm( request.POST , request.FILES ,
                                instance=request.user.profile )
        user_form = UserForm( request.POST , instance=request.user)
        location_form = LocationForm( request.POST ,
                                    instance=request.user.profile.location)
        # so in all forms we send the request post data to the form to be assigned
        # and the request files to assign the meida files also
        if profile_form.is_valid() and user_form.is_valid() and location_form.is_valid():
            profile_form.save()
            location_form.save()
            user_form.save()
            user_liked_listings = LikedListing.objects.filter(
                profile = request.user.profile)
            messages.success(request , f'Changes Done Successfully !')
        else : 
            messages.error(request , f'Invalid data submitted !!')
        context = {
            'profile_form' : profile_form  , 
            'user_form' : user_form , 
            'location_form' : location_form , 
            'user_listings' : user_listings ,
            'user_liked_listings' : user_liked_listings ,
        }
        return render(request , 'views/profile.html' , context)
    
