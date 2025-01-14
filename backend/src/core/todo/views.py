from django.shortcuts import render
from rest_framework import viewsets
from core.todo.serializers import TodoSerializer
from core.todo.models import Todo


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
