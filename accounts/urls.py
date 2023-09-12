from django.urls import path, include

name_app='accounts'


urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    
      
]