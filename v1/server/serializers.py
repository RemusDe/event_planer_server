from rest_framework import serializers
from .models import Task
from .models import Order


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'order', 'title', 'description', 'status')


class OrderSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'title', 'description', 'status', 'date', 'tasks')
