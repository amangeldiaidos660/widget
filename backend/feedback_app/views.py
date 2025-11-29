from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import serializers

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
