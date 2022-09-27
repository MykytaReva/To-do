from django.db import models
from todo.model_choices import Status
from django.contrib.auth.models import User


class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    subject = models.CharField(max_length=100)
    date_todo = models.DateField()
    when = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.STATUS_INPROCESS
    )
