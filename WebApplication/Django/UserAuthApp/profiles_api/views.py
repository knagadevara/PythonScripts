from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

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
            

    
    


     
