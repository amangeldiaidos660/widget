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
        'created_at',
        'short_console_logs',
        'short_network_errors',
        'short_js_errors',
    ]
    list_filter = ['status', 'project', 'created_at', 'assigned_to']
    search_fields = [
        'ticket_id',
        'author_name',
        'author_email',
        'author_login',
        'description',
        'console_logs',
        'network_errors',
        'js_errors',
    ]
    readonly_fields = ['ticket_id', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    raw_id_fields = ['project', 'assigned_to']
    fieldsets = (
        (None, {
            'fields': (
                'ticket_id', 'project', 'status', 'author_name', 'author_email', 'author_login',
                'description', 'page_url', 'user_agent', 'screen_resolution',
                'console_logs', 'network_errors', 'js_errors',
                'assigned_to', 'created_at', 'updated_at'
            )
        }),
    )

    def short_console_logs(self, obj):
        return (obj.console_logs[:75] + '...') if obj.console_logs and len(obj.console_logs) > 75 else obj.console_logs
    short_console_logs.short_description = 'console_logs'

    def short_network_errors(self, obj):
        return (obj.network_errors[:75] + '...') if obj.network_errors and len(obj.network_errors) > 75 else obj.network_errors
    short_network_errors.short_description = 'network_errors'

    def short_js_errors(self, obj):
        return (obj.js_errors[:75] + '...') if obj.js_errors and len(obj.js_errors) > 75 else obj.js_errors
    short_js_errors.short_description = 'js_errors'


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
