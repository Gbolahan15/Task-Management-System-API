from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
    
'''
This is to ensure task ownership security 
A user can ONLY  view, edit, and delete their own tasks.
'''