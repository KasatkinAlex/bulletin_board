from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = 'Вы не являетесь создателем'

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        else:
            return False


class IsAdmin(permissions.BasePermission):
    message = 'Вы не являетесь администраторм'

    def has_object_permission(self, request, view, obj):
        if request.user.role in "admin":
            return True
        else:
            return False
