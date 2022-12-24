from django.db import models
from django.contrib.auth.models import User


class TodoItem(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
