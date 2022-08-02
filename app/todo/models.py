from django.db import models
from todo.model_choices import Status

class ToDo(models.Model):

    subject = models.CharField(max_length=100)
    date_todo = models.DateField()
    when = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.STATUS_INPROCESS
    )
