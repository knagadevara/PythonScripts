from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework import status , viewsets , filters
## To Generate and obtain Authentication Token
from rest_framework.authtoken.views import ObtainAuthToken
## Allows users to authenticate with the api
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
##
from rest_framework.permissions import IsAuthenticated
## Application classes
from profiles_api import serializers , models , permissions

class HelloAPIView(APIView):
    """ Test api View, application logic for the endpoint will be defined """

    ## mapping the custom serializer to the URL and Class: HelloAPIView 
    serializer_class = serializers.HelloSerializer

    def get(self, request , format=None):
        """ executes the below code and returns with response list of APIViews """

        an_apiview = [
            'Similar to Django but specific to API',
            'Uses HTTP functions(get, post, patch, put, delete)',
            'Mapped manually to urls.py',
        ]
        ## When API is called it returns an objects as JSON data., but it is mostly fed either a dictionary or list(which would automatically be converted to json.)
        return Response(data = {'message': 'Hello!!' , 'an_apiview' : an_apiview})
    

    def post(self, request):
        """ Creats a Hello message with variable name """
        ## retrieve configured serializer is via serializer_class from APIView -> parse data which is posted in the passed 'request' -> save it to variable 
        serializer_hello = self.serializer_class(data=request.data)
        ## Validata the data(contents) through the rules set in accordance with serializer.py
        if serializer_hello.is_valid():
            name = serializer_hello.validated_data.get('name')
            message = 'Hello {0}, type: {1}'.format(name,type(name))
            return Response({'message': message})
        else:
            ## returning the errors if serializer_hello is not as per the defined rules in serializers.py
            ## returning the HTTP status
            return Response(serializer_hello._errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request , pk=None):
        return Response({'method' : 'PUT'})

    def patch(self, request , pk=None):
        return Response({'method' : 'PATCH'})

    def delete(self, request , pk=None):
        return Response({'method' : 'DELETE'})
            

class HelloViewSet(viewsets.ViewSet):
    """ Test ViewSet """
    
    serialiser_class = serializers.HelloSerializer

    def list(self, request):
        """ lists the features of APIvIEWSEt"""

        a_viewset = [
            'Uses Actions (LIST,CREATE,RETRIEVE,UPDATE,PARTIAL_UPDATE)',
            'Automatic mapping using URL Routers',
            'Provides more functionality with less code'

        ]
        return Response({'message': 'Hello!', 'ViewSet' : a_viewset})

    def create(self, request):
        """ Retrive the data provided in the request through serialization and validate it """
        request_data = self.serialiser_class(data=request.data)
        if request_data.is_valid():
            name = request_data.validated_data.get('name')
            message = f'Hello! {name}'
            return Response({'message': message})
        else:
            return Response(request_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request, pk=None):
        """ Retrieves an object with matched id """
        return Response({'http_method' : 'GET'})
    
    def update(self, request,pk=None):
        """ Overwites the old value """
        return Response({'http_method':'PUT'})
    
    def partial_update(self, request,pk=None):
        return Response({'http_method':'PATCH'})
    
    def destroy(self, request, pk=None):
        return Response({'http_method':'DELETE'})
### , SessionAuthentication, BasicAuthentication,
class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    ## Queryset is enabled on all the classes/methods in models.py
    queryset = models.UserProfile.objects.all()
    ## adding the type of functionality to authenticate
    authentication_classes = (TokenAuthentication,)
    ## Adding permissions
    permission_classes = (permissions.UpdateOwnProfile,)
    ## Filtering functionality
    filters_backend = (filters.SearchFilter,)
    search_fields = ('username' , 'email',)
#    render_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserLoginApiView(ObtainAuthToken):
    """ Handle creation of Authentication Token """
    ## The way to aquire the credentials are example: curl -X POST  -d "username=wer21@cba.com&password=54321"  http://localhost:8000/api/login/
    render_classes = api_settings.DEFAULT_RENDERER_CLASSES

## Communicates with database do inheriting Modelviewset
## SessionAuthentication, BasicAuthentication, is removed for now
class UserProfileFeedItemViewSet(viewsets.ModelViewSet):
    """ Handels creating, reading and updating profiles feed item """
    serializer_class = serializers.ProfileFeedItemSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnFeedItem, IsAuthenticated)
    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)