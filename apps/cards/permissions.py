from rest_framework.permissions import BasePermission, SAFE_METHODS


class CardsPermissons(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request in SAFE_METHODS:
            return True
        
        return request.user.is_authenticated and request.user.is_owner