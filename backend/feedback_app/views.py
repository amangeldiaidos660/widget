from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Ticket

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

@api_view(["GET"])
def health(request):
	return Response({"status": "ok"})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def current_user(request):
	"""Эндпоинт для получения информации о текущем пользователе"""
	serializer = UserSerializer(request.user)
	return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def staff_users(request):
	"""Эндпоинт для получения списка staff пользователей (сотрудников)"""
	staff_users_list = User.objects.filter(is_staff=True).order_by('username')
	serializer = UserSerializer(staff_users_list, many=True)
	return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard_stats(request):
	"""Статистика для дашборда"""
	tickets = Ticket.objects.all()
	
	# Фильтр по проекту если указан
	project_slug = request.query_params.get('project')
	if project_slug:
		tickets = tickets.filter(project__slug=project_slug)
	
	return Response({
		'total': tickets.count(),
		'new': tickets.filter(status='NEW').count(),
		'in_progress': tickets.filter(status='IN_PROGRESS').count(),
		'closed': tickets.filter(status='CLOSED').count(),
	})
