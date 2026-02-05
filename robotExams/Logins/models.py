from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', default=None)
#     device_id = models.CharField(max_length=255, blank=True, null=True)
#     questionArray = models.JSONField(default=list, blank=True)
#     answerArray = models.JSONField(default=list, blank=True)

#     def __str__(self):
#         return self.user.username