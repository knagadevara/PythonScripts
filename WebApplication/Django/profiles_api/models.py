from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ Manager for User Profiles Overiding the System defined parameters to custom defined """

    def create_User(self, email , name , password=None):
        """ Create a new user Profile """
        if not email:
            raise ValueError('Mandate fileld,\: should have an email address')
        else:
            email = self.normalize_email(email)
            user = self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_SuperUser(self, email, name, password):
        """ Create a new super user """
        user = self.create_User(email,name,password)
        user.is_superuser = True    #### Variable inhereted from PermissionsMixin, case sensitive
        user.is_Staff = True
        user.save(using=self._db)



class UserProfiles(AbstractBaseUser , PermissionsMixin):
    """ Imported AbstractBaseUser , PermissionsMixin methods to add some of functionality and override
        We are creating a model-> which creates the required DB table automatically with the fields that ae provided here.
    """

    user_Email = models.EmailField(unique=True, max_length=254)
    first_Name = models.CharField(max_length=50)
    last_Name = models.CharField(max_length=50)
    is_Staff = models.BooleanField(default = False)
    is_Active = models.BooleanField(default = True )

    def get_FullName(self):
        return '{0} {1}'.format(self.first_Name , self.last_Name)

    def ger_UserEmailAddress(self):
        return self.user_Email
    
    objects = UserProfileManager()

    USERNAME_FIELD = 'user_Email'
    REQUIRED_FIELD = ['first_Name', 'last_Name']
    
    def __str__(self):
        return self.get_FullName()