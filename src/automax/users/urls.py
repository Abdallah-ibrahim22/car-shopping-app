from django.urls import path 
from .views import login_view , RegisterView , logout_view , Profile_view
urlpatterns = [
    path('login/' , login_view , name='login'),
    path('register/' , RegisterView.as_view() , name='register'),
    # (as_view() : used for class based views)
    path('logout/' , logout_view , name='logout'),
    path('profile/' , Profile_view.as_view() , name='profile'),
]
