from django.db import models

class Status(models.TextChoices):
    STATUS_INPROCESS = 'Active', 'In process'
    STATUS_DONE = 'Completed', 'Done'
