## The requests that begin with "api/" as a prefix will be responded from here 'profiles_api.urls'
## This file contains all the suffixe/sublink forwards
from django.urls import path , include
from rest_framework.routers import DefaultRouter 
from profiles_api import views

router = DefaultRouter()
router.register('hello_viewset' , views.HelloViewSet , basename='hello_viewset')

urlpatterns = [
    path('hello_api/' , views.HelloAPIView.as_view()),
    path('' , include(router.urls))
]
