from django.contrib import admin

## Adding the userdefined model to admin
from profiles_api import models
# Register your models here.

admin.site.register(models.UserProfiles)
