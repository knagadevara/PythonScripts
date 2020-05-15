from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

## importing most of the functionality with BaseUserManager
class UserProfileManager(BaseUserManager):
    """ Custome Manager for User Profiles Overiding the System defined parameters, which makes Django to interact with the fields """

    ## Beaware that all the method names and variables are case sensitive.

    def create_user(self, email , username , password , first_name , last_name):
        """ Create a new user Profile """
        if not email:
            raise ValueError('Mandate fileld: should have an email address')
        if not password:
            raise ValueError("User must have a password")
        if not username:
            raise ValueError("User must have a full name")
        else:
            email = self.normalize_email(email)
            first_name = str(first_name).lower()
            last_name = str(last_name).lower()
            ## Injecting values into the user table with any given required fields which are recgnized by the model
            ## self will be ointing at the current instance of the call which is a unique meemory address until solidifies
            user = self.model(email=email , username=username , first_name=first_name , last_name=last_name)
        ## sets user password as an encrypted hash value
        user.set_password(password)
        ## in normal cases driver of the database is provided to lock it to single DB but '_db' would make the model to be used on multiple DB's 
        ## also at a user will be created at this point when 'save' is called[ solidified ]
        user.save(using=self._db)      
        ## Return the user object to the method
        return user
    
    def create_superuser(self, email, username, password , first_name , last_name): #### Method is case sensitive
        """ Create a new super user """
        ## Calling create-user function, with mandatory positional parameters.
        ## the function will save the instanciated object with the values in the variable user <- as superuser in the same user table. 
        user = self.create_user(email,username,password, first_name , last_name)
        ## Predefined Variable mapped to the inhereted PermissionsMixin class, case sensitive
        user.is_superuser = True
        ## User defined Parameter which is always True or SuperUser part of userProfile class
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser , PermissionsMixin):
    """ Imported AbstractBaseUser , PermissionsMixin methods to add some of functionality and override
        We are creating a model-> which creates the required DB table automatically with the fields that ae provided here.
    """
    
    ## this is to override the default username filed in AbstractBaseUser Super class.
    ## Creates an email collumn in the database which is unique and its tyoe is Email
    email = models.EmailField(unique=True, max_length=64)
    ## Creates 'username' column of character type
    username = models.CharField(unique=True, max_length=64)
    ## Nameof the user
    first_name =  models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    ##  The below colums are for security and permission concerns, overriding the functionality of PermissionMixin
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True )

    ## Custome userprofile manager to override the default
    objects = UserProfileManager()
    # Overriding the default username field to email
    USERNAME_FIELD = 'email'
    ## required field
    REQUIRED_FIELDS = [ 'username', 'first_name' , 'last_name' ]

    def get_FullName(self):
        return '{1} {0}'.format(self.first_name , self.username)

    def ger_UserEmailAddress(self):
        return self.email
    
    def __str__(self):
        """ Returns the string representation of the User """
        return self.get_FullName()