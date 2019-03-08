from django.db import models
#from django.contrib.auth.models import User


class Order(models.Model):
    PLANNED = 0
    ACTIVE = 1
    EXPIRED = 2

    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (EXPIRED, 'Expired'),
        (PLANNED, 'Planed'),
    )

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS_CHOICES, default=PLANNED)
    date = models.DateField(auto_now_add=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Task(models.Model):
    DONE = 1
    PROCEED = 0

    STATUS_CHOICES = (
        (DONE, 'Done'),
        (PROCEED, 'Proceed')
    )

    order = models.ForeignKey(Order, related_name='tasks', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS_CHOICES, default=PROCEED)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
