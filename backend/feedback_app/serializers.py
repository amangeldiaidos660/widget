from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Project, Ticket, Attachment, Comment
from datetime import datetime


class ProjectSerializer(serializers.ModelSerializer):
    """Сериализатор проекта (read-only для виджета)"""
    
    class Meta:
        model = Project
        fields = ['id', 'name', 'slug', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']


class AttachmentSerializer(serializers.ModelSerializer):
    """Сериализатор вложения (file → URL)"""
    file_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Attachment
        fields = ['id', 'ticket', 'file', 'file_url', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at']
    
    def get_file_url(self, obj):
        """Возвращает полный URL файла"""
        request = self.context.get('request')
        if obj.file and request:
            return request.build_absolute_uri(obj.file.url)
        return None


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор комментария (author username + avatar)"""
    author_username = serializers.CharField(source='author.username', read_only=True)
    author_email = serializers.EmailField(source='author.email', read_only=True)
    author_avatar = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id', 'ticket', 'author', 'author_username', 'author_email', 
                  'author_avatar', 'text', 'created_at']
        read_only_fields = ['id', 'author', 'author_username', 'author_email', 
                           'author_avatar', 'created_at']
    
    def get_author_avatar(self, obj):
        """Возвращает URL аватара пользователя (можно расширить позже)"""
        # Пока возвращаем None, можно добавить логику для получения аватара
        return None


class TicketListSerializer(serializers.ModelSerializer):
    """Краткий сериализатор заявки для списка"""
    project_name = serializers.CharField(source='project.name', read_only=True)
    project_slug = serializers.CharField(source='project.slug', read_only=True)
    assigned_to_username = serializers.CharField(
        source='assigned_to.username', 
        read_only=True,
        allow_null=True
    )
    
    class Meta:
        model = Ticket
        fields = [
            'id', 'ticket_id', 'project', 'project_name', 'project_slug',
            'status', 'author_name', 'author_email', 'description',
            'assigned_to', 'assigned_to_username', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'ticket_id', 'created_at', 'updated_at']


class TicketDetailSerializer(serializers.ModelSerializer):
    """Полный сериализатор заявки с вложенными attachments и comments"""
    project_name = serializers.CharField(source='project.name', read_only=True)
    project_slug = serializers.CharField(source='project.slug', read_only=True)
    assigned_to_username = serializers.CharField(
        source='assigned_to.username', 
        read_only=True,
        allow_null=True
    )
    attachments = AttachmentSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Ticket
        fields = [
            'id', 'ticket_id', 'project', 'project_name', 'project_slug',
            'status', 'author_name', 'author_email', 'author_login',
            'description', 'page_url', 'user_agent', 'screen_resolution',
            'console_logs', 'network_errors', 'js_errors',  # <-- добавить эти поля
            'assigned_to', 'assigned_to_username', 'created_at', 'updated_at',
            'attachments', 'comments'
        ]
        read_only_fields = ['id', 'ticket_id', 'created_at', 'updated_at']


class TicketCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания заявки от виджета (без assigned_to)"""
    project_slug = serializers.SlugField(write_only=True)
    
    class Meta:
        model = Ticket
        fields = [
            'project_slug', 'author_name', 'author_email', 'author_login',
            'description', 'page_url', 'user_agent', 'screen_resolution'
        ]
    
    def validate_project_slug(self, value):
        """Проверяет, что проект существует и активен"""
        try:
            project = Project.objects.get(slug=value, is_active=True)
        except Project.DoesNotExist:
            raise serializers.ValidationError(
                f"Проект со slug '{value}' не найден или неактивен"
            )
        return value
    
    def create(self, validated_data):
        """Создаёт заявку с автоматической генерацией ticket_id"""
        project_slug = validated_data.pop('project_slug')
        project = Project.objects.get(slug=project_slug)
        
        # Генерируем ticket_id в формате TICKET-YYYY-XXXX
        current_year = datetime.now().year
        last_ticket = Ticket.objects.filter(
            ticket_id__startswith=f'TICKET-{current_year}-'
        ).order_by('-ticket_id').first()
        
        if last_ticket:
            # Извлекаем номер из последнего ticket_id
            try:
                last_number = int(last_ticket.ticket_id.split('-')[-1])
                next_number = last_number + 1
            except (ValueError, IndexError):
                next_number = 1
        else:
            next_number = 1
        
        ticket_id = f'TICKET-{current_year}-{next_number:04d}'
        
        # Создаём заявку
        ticket = Ticket.objects.create(
            project=project,
            ticket_id=ticket_id,
            status='NEW',
            **validated_data
        )
        
        return ticket

