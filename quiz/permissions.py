from rest_framework import permissions
class IsAuthor(permissions.BasePermission):
    """
    Object-level permission to only allow author of an object to edit it.
    Assumes the model instance has an `author` attribute.
    """

    def has_object_permission(self, request, view, obj):
        

        # Instance must have an attribute named `owner`.
        return obj.author == request.user