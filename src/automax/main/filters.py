import django_filters 

from main.models import Listing

class ListingFilter(django_filters.FilterSet):
    
    class Meta :
        model = Listing
        fields = {'brand':{'exact'},'transmission':{'exact'},}
        # here we decide the field that we want to filter the objs with
        # (exact) means to get the object that content this exact value 
        # i enter in any field that i mentioned in the fields attr
        exclude = ('',)