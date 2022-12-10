from django.db import models


class TodoItem(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
