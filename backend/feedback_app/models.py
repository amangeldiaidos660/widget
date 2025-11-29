from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Project(models.Model):
    """Модель проекта/приложения"""
    name = models.CharField(max_length=255, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})


class ResponsibleMapping(models.Model):
    """Модель связи проекта и ответственного пользователя"""
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='responsible_mappings',
        verbose_name="Проект"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='responsible_projects',
        verbose_name="Пользователь"
    )

    class Meta:
        verbose_name = "Ответственный за проект"
        verbose_name_plural = "Ответственные за проекты"
        unique_together = [['project', 'user']]
        ordering = ['project', 'user']

    def __str__(self):
        return f"{self.project.name} - {self.user.username}"


class Ticket(models.Model):
    """Модель заявки/тикета"""
    STATUS_CHOICES = [
        ('NEW', 'Новая'),
        ('IN_PROGRESS', 'В работе'),
        ('CLOSED', 'Закрыта'),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tickets',
        verbose_name="Проект"
    )
    ticket_id = models.CharField(
        max_length=50,
        unique=True,
        db_index=True,
        verbose_name="ID заявки"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='NEW',
        verbose_name="Статус"
    )
    author_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Имя автора"
    )
    author_email = models.EmailField(
        null=True,
        blank=True,
        verbose_name="Email автора"
    )
    author_login = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Логин автора"
    )
    description = models.TextField(verbose_name="Описание")
    page_url = models.CharField(
        max_length=2048,
        null=True,
        blank=True,
        verbose_name="URL страницы"
    )
    user_agent = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        verbose_name="User Agent"
    )
    screen_resolution = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Разрешение экрана"
    )
    console_logs = models.TextField(blank=True, null=True, verbose_name="Логи консоли")
    network_errors = models.TextField(blank=True, null=True, verbose_name="Сетевые ошибки")
    js_errors = models.TextField(blank=True, null=True, verbose_name="JS-ошибки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создана")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлена")
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tickets',
        verbose_name="Назначена на"
    )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['ticket_id']),
            models.Index(fields=['status']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.ticket_id} - {self.project.name}"

    def get_absolute_url(self):
        return reverse('ticket-detail', kwargs={'pk': self.pk})


class Attachment(models.Model):
    """Модель вложения к заявке"""
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name='attachments',
        verbose_name="Заявка"
    )
    file = models.FileField(
        upload_to='tickets/%Y/%m/%d/',
        verbose_name="Файл"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Загружен")

    class Meta:
        verbose_name = "Вложение"
        verbose_name_plural = "Вложения"
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.ticket.ticket_id} - {self.file.name}"

    def get_absolute_url(self):
        return reverse('attachment-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    """Модель комментария к заявке"""
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Заявка"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Автор"
    )
    text = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['created_at']

    def __str__(self):
        return f"{self.ticket.ticket_id} - {self.author.username} - {self.created_at}"

    def get_absolute_url(self):
        return reverse('comment-detail', kwargs={'pk': self.pk})
