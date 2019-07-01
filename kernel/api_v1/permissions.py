from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response

import logging
logger = logging.getLogger(__name__)



class RegisterPermission(BasePermission):
    def has_permission(self, request, view):
        return True

class NoPermission(BasePermission):
    def has_permission(self, request, view):
        return True

class NormalPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS:
                return True
            return bool(request.user and request.user.is_staff)

class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        
class UserNestedProfilePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.profile.user:
            return True

class UserMachinePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.driver.profile.user:
            return True

class UserProfilePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
