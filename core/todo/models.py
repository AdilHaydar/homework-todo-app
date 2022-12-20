from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, 
        blank=False, related_name='todos'
        )
    title = models.CharField(
        max_length=64, null=False, blank=False
        )
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.get_full_name}: {self.title}"
    
    
    