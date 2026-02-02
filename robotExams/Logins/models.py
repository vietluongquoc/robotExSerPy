from django.db import models

# Create your models here.
class   UserProfile(models.Model):
    user_name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    last_login = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=128)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    questionArray = models.JSONField(default=list, blank=True)
    answerArray = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.user_name