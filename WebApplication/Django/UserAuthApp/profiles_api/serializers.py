from rest_framework import serializers
## Import the models package from the application where the classes are present
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """ Serializer for a name field for testing APIView """
    name = serializers.CharField(max_length = 10)

## A model serializer will give functionality to the interact with existing Database Models/Tables related to Django application

class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes the UserProfile object """
    ## defining a metaclass to Configure a sprcific models.UserProfile to created serializer
    class Meta():
        """ sets out the class to point at the UserProfile model """
        model = models.UserProfile
        ## Specify the fields that are to be used/accessable by the umodel serializer to API endpoint.
        ## Creating a Tuple [ as it is immutable ] of fields available in the model/db
        fields = ('id' , 'email' , 'username' , 'password' , 'first_name' , 'last_name')
        ## To restrict the password to be retrieved by users altering the default field configuration
        ## achieved by declaring the properties in a extra_kwargs for the specific field.
        ## Allowing Write_only , setting the styling to password '******' 
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'style' : {'input':'password'}
            }
        } 
    
    ## Overriding the default create function which uses objectManager to use create_user function Models
    ## When an object of 'UserProfileSerializer' is called the data will be validated and passed on to create function
    def create(self, validated_data):
        """ create and return new user """
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            username = validated_data['username'],
            password = validated_data['password'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )

        return user
