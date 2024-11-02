from django.urls import path
from main import views
urlpatterns = [
    path('',views.landing_view , name='main') ,
    path('home/',views.home_view , name='home') ,
    path('list/',views.list_view , name='list') ,
    path('listing/<str:id>/',views.listing_view , name='listing') ,
    # this id attr we should assign it in our template 
    # as (id = Listing.id) after the name of the url
    path('listing/<str:id>/edit',views.edit_view , name='edit') ,
    path('listing/<str:id>/like',views.like_wiew , name='like') ,
]
