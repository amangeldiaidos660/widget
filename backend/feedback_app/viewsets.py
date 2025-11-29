from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as django_filters
from django.db.models import Q

from .models import Project, Ticket, Attachment, Comment
from .serializers import (
    ProjectSerializer,
    TicketListSerializer,
    TicketDetailSerializer,
    TicketCreateSerializer,
    AttachmentSerializer,
    CommentSerializer
)
from .permissions import IsAdminOrReadOnly, IsAssignedOrAdmin, IsAuthenticatedForWrite


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet для проектов (только чтение, только активные для виджета).
    """
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'slug'


class TicketFilter(django_filters.FilterSet):
    """Фильтры для заявок"""
    project__slug = django_filters.CharFilter(field_name='project__slug', lookup_expr='exact')
    status = django_filters.ChoiceFilter(choices=Ticket.STATUS_CHOICES)
    assigned_to = django_filters.NumberFilter(field_name='assigned_to')
    created_at__date = django_filters.DateFilter(field_name='created_at', lookup_expr='date')
    search = django_filters.CharFilter(method='filter_search')
    
    class Meta:
        model = Ticket
        fields = ['project__slug', 'status', 'assigned_to', 'created_at__date']
    
    def filter_search(self, queryset, name, value):
        """Поиск по ticket_id, описанию, email автора"""
        return queryset.filter(
            Q(ticket_id__icontains=value) |
            Q(description__icontains=value) |
            Q(author_email__icontains=value) |
            Q(author_name__icontains=value)
        )


class TicketViewSet(viewsets.ModelViewSet):
    """
    ViewSet для заявок.
    - list + фильтры (project, status, assigned_to, search)
    - retrieve
    - create (доступно анониму/виджету)
    - partial_update (только для сотрудников: status, assigned_to)
    - destroy (опционально)
    """
    queryset = Ticket.objects.all()
    permission_classes = [IsAuthenticatedForWrite]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = TicketFilter
    search_fields = ['ticket_id', 'description', 'author_email', 'author_name']
    ordering_fields = ['created_at', 'updated_at', 'status']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        """Выбираем сериализатор в зависимости от действия"""
        if self.action == 'create':
            return TicketCreateSerializer
        elif self.action == 'list':
            return TicketListSerializer
        elif self.action == 'retrieve':
            return TicketDetailSerializer
        return TicketDetailSerializer
    
    def get_permissions(self):
        """Настраиваем права доступа в зависимости от действия"""
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAssignedOrAdmin()]
        return super().get_permissions()
    
    def create(self, request, *args, **kwargs):
        """Создание заявки (доступно анониму)"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ticket = serializer.save()
        
        # Возвращаем полный объект с детальным сериализатором
        detail_serializer = TicketDetailSerializer(
            ticket,
            context={'request': request}
        )
        return Response(
            detail_serializer.data,
            status=status.HTTP_201_CREATED
        )
    
    def partial_update(self, request, *args, **kwargs):
        """Частичное обновление (только status и assigned_to для сотрудников)"""
        ticket = self.get_object()
        
        # Разрешаем изменять только status и assigned_to
        allowed_fields = ['status', 'assigned_to']
        data = {k: v for k, v in request.data.items() if k in allowed_fields}
        
        # Используем TicketDetailSerializer для обновления
        serializer = TicketDetailSerializer(ticket, data=data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        """Удаление заявки (позже можно сделать soft-delete)"""
        return super().destroy(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet для комментариев.
    - create/list только в рамках ticket
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAssignedOrAdmin]
    filter_backends = [DjangoFilterBackend]
    
    def get_queryset(self):
        """Фильтруем комментарии по ticket_id"""
        queryset = Comment.objects.all()
        ticket_id = self.request.query_params.get('ticket', None)
        if ticket_id:
            queryset = queryset.filter(ticket__ticket_id=ticket_id)
        return queryset
    
    def perform_create(self, serializer):
        """Автоматически устанавливаем автора комментария"""
        serializer.save(author=self.request.user)


class AttachmentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet для вложений (только чтение).
    """
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    
    def get_queryset(self):
        """Фильтруем вложения по ticket_id"""
        queryset = Attachment.objects.all()
        ticket_id = self.request.query_params.get('ticket', None)
        if ticket_id:
            queryset = queryset.filter(ticket__ticket_id=ticket_id)
        return queryset

