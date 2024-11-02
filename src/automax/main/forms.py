from django import forms 
from main.models import Listing 

class ListingForm(forms.ModelForm):

    image = forms.ImageField()
    class Meta:
        model = Listing
        fields = {'brand' , 'model' , 'description' , 'engine' , 'transmission' ,
                'vin' , 'mileage' , 'color' , 'image'}
        
