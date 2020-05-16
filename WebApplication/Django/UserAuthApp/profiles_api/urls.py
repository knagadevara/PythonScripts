## The requests that begin with "api/" as a prefix will be responded from here 'profiles_api.urls'
## This file contains all the suffixe/sublink forwards
from django.urls import path
from profiles_api import views

urlpatterns = [
    path('hello_api/' , views.HelloAPIView.as_view()),  
]
