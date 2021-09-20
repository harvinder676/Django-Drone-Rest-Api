from rest_framework import permissions

class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            # The method is a safe method
            return True
        else:
            #the method isn't safe method
            # only users are granted permission for unsafe method
            return obj.owner == request.user    # Cheking whether user is owner or not
