from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Разрешение: только чтение для всех, изменение только для администраторов.
    """
    
    def has_permission(self, request, view):
        # GET, HEAD, OPTIONS разрешены всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Остальные методы только для администраторов
        return request.user and request.user.is_staff


class IsAssignedOrAdmin(permissions.BasePermission):
    """
    Разрешение: изменение статуса и комментариев только для назначенных сотрудников или администраторов.
    """
    
    def has_object_permission(self, request, view, obj):
        # Чтение разрешено всем
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Для Ticket: проверяем, назначена ли заявка на пользователя или он админ
        from .models import Ticket, Comment
        if isinstance(obj, Ticket):
            return (
                request.user.is_authenticated and
                (request.user.is_staff or obj.assigned_to == request.user)
            )
        
        # Для Comment: проверяем, назначена ли заявка на пользователя или он админ
        if isinstance(obj, Comment):
            ticket = obj.ticket
            return (
                request.user.is_authenticated and
                (request.user.is_staff or ticket.assigned_to == request.user)
            )
        
        # По умолчанию только для администраторов
        return request.user and request.user.is_staff


class IsAuthenticatedForWrite(permissions.BasePermission):
    """
    Разрешение: создание заявки разрешено всем (включая анонимов),
    остальные операции только для аутентифицированных пользователей.
    """
    
    def has_permission(self, request, view):
        # Создание заявки (POST) разрешено всем
        if view.action == 'create' and view.basename == 'ticket':
            return True
        
        # Чтение разрешено всем
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Остальные операции только для аутентифицированных
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        # Чтение разрешено всем
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Изменение только для аутентифицированных
        return request.user and request.user.is_authenticated

