from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAnnouncerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.publisher == request.user

class IsContractorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view,obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user ==  obj.user
