from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(unique=True, null=False)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(unique=True, null=False)
    def __str__(self):
        return self.name

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(null=False, max_length=200)
    description = models.CharField(null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    tag = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)
    due_date = models.DateField()
    class Status(models.TextChoices):
        NEW = 'nw', 'New'
        IN_PROGRESS = 'ip', 'In Progress'
        COMPLETED = 'cm', 'Completed'
    status = models.CharField(choices=Status, default=Status.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


