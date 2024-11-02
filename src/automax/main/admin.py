from django.contrib import admin
from .models import Listing , LikedListing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    # to decide which field we wanna show as readonly field  

class LikedListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    # to decide which field we wanna show as readonly field  

admin.site.register(Listing,ListingAdmin)
admin.site.register(LikedListing,LikedListingAdmin)
