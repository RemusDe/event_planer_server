from .models import Task
from .models import Order
from .serializers import TaskSerializer
from .serializers import OrderSerializer

# Import django rest framework functions

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

#importing the views we created
from . import views


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    authentication_classes = (BasicAuthentication,)
    #permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()  # Select all taks
    serializer_class = TaskSerializer  # Serialize data


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    authentication_classes = (BasicAuthentication,)
    #permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()  # Select all taks
    serializer_class = OrderSerializer  # Serialize data

