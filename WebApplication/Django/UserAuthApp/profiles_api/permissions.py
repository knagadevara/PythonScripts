from rest_framework import permissions

## Making a custom permission class to restrict users from editing the details of other users
class UpdateOwnProfile(permissions.BasePermission):
    """ Allow users to edit their own profile """

    ## Method gets called every time a request is made to the api ths permission class is assigned to
    ## It will return a boolean value [True or False] basing on whether user/entity have correct permissions 
    ## on the fields in the table they are trying to change  
    def has_object_permission(self, request, view, obj):
        """ Check if user is trying to edit their own profile """
        ## Adding the checks below to see if the request is in SAFE_METHOD i.e GET
        if request.method in permissions.SAFE_METHODS:
            return True      
        ## Evaluates if the id is same as the id of row where the firelds are changing
        return obj.id == request.user.id

class UpdateOwnFeedItem(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True      
        ## Evaluates if the id is same as the id of row where the firelds are changing
        return obj.user_profile.id == request.user.id