from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class Todo(models.Model):

    SCHEDULE = 1
    DO_FIRST = 2
    DELEGATE = 3
    DO_NOT_DO = 4

    QUAD_CHOICES = [
        (SCHEDULE, "Schedule"),
        (DO_FIRST, "Do First"),
        (DELEGATE, "Delegate"),
        (DO_NOT_DO, "Do Not Do"),
    ]

    user = models.ForeignKey(User, on_delete=CASCADE)
    quad = models.IntegerField(verbose_name="Quadrant", choices=QUAD_CHOICES)
