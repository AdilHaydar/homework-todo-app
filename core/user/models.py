from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class LoginInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='login_informations')
    description = models.JSONField(null=True, blank=True)
    login_at = models.DateTimeField(auto_now_add = True)
    is_success = models.BooleanField()
    remote_addr = models.GenericIPAddressField(null=True, blank=True)