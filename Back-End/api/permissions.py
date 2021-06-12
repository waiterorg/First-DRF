from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    """
    Allows access only to super users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)

class IsStaffOrReadOnly(BasePermission):
    """
    The request is authenticated as a staff user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )

class IsAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # get access to superuser or author.
        return bool(
            request.user.is_authenticated and request.user.is_superuser or
            request.user.is_authenticated and obj.author == request.user
        )

class IsSuperUserOrStaffReadOnly(BasePermission):

    def has_permission(self, request, view):
        #get access to superuser and read only to staff user.
        return bool(
            request.method in SAFE_METHODS and request.user and request.user.is_staff or
            request.user and
            request.user.is_superuser
        )