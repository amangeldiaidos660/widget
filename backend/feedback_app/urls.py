from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ProjectViewSet,
    TicketViewSet,
    CommentViewSet,
    AttachmentViewSet
)

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'tickets', TicketViewSet, basename='ticket')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'attachments', AttachmentViewSet, basename='attachment')

urlpatterns = [
    path('', include(router.urls)),
]

