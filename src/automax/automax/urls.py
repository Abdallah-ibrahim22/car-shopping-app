"""
URL configuration for automax project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
# to import the settings file 
from django.conf.urls.static import static
# here to make us able to apply url for static files when we call it on the site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('users.urls')),
    # so here we link the urls for each app we created
] 
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
# here to add a url for the media so when we call it we go to the documet_root 
# which is points to the media_root
