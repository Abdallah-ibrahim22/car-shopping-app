from django import forms 
from users.models import Location , Profile
from django.contrib.auth.models import User
from localflavor.us.forms import USZipCodeField
from users.widgets import CustomPicImgFieldWidget


class UserForm(forms.ModelForm):

    username = forms.CharField(disabled=True)
    # to make the user doesn't have the ability to change his username
    class Meta:
        model = User
        fields = ('username' , 'first_name' , 'last_name' , 'email')

class ProfileForm(forms.ModelForm):
    
    photo = forms.ImageField(widget=CustomPicImgFieldWidget())
    class Meta :
        model = Profile 
        fields = ('photo' , 'bio' , 'number')

class LocationForm(forms.ModelForm) :
    address_1 = forms.CharField(required=True)
    zip_code = USZipCodeField(required = True)

    class Meta:
        model = Location
        fields = '__all__'
        exclude = ('',)