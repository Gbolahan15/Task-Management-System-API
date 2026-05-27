from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # many tasks can belong to ONE category
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True) 

    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title