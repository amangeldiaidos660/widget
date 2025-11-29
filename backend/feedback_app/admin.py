from django.contrib import admin
from .models import Project, ResponsibleMapping, Ticket, Attachment, Comment


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at']


@admin.register(ResponsibleMapping)
class ResponsibleMappingAdmin(admin.ModelAdmin):
    list_display = ['project', 'user']
    list_filter = ['project']
    search_fields = ['project__name', 'user__username']


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = [
        'ticket_id',
        'project',
        'status',
        'author_name',
        'author_email',
        'assigned_to',
        'created_at'
    ]
    list_filter = ['status', 'project', 'created_at', 'assigned_to']
    search_fields = [
        'ticket_id',
        'author_name',
        'author_email',
        'author_login',
        'description'
    ]
    readonly_fields = ['ticket_id', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    raw_id_fields = ['project', 'assigned_to']


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'file', 'uploaded_at']
    list_filter = ['uploaded_at']
    search_fields = ['ticket__ticket_id', 'file']
    readonly_fields = ['uploaded_at']
    raw_id_fields = ['ticket']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'author', 'created_at']
    list_filter = ['created_at', 'author']
    search_fields = ['ticket__ticket_id', 'author__username', 'text']
    readonly_fields = ['created_at']
    raw_id_fields = ['ticket', 'author']
    date_hierarchy = 'created_at'
