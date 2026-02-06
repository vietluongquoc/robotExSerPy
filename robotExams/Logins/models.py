from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class examDb(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', default=None)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    questionArray = models.JSONField(default=list, blank=True)
    answerArray = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.user.username


class questionDb(models.Model):
    id = models.AutoField(primary_key=True)
    questiontype = models.CharField(max_length=50)
    questionText = models.TextField()
    ispicture = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='questions/', blank=True, null=True)
    optionA = models.CharField(max_length=255)
    optionB = models.CharField(max_length=255, blank=True)
    optionC = models.CharField(max_length=255, blank=True)
    optionD = models.CharField(max_length=255, blank=True)
    correctAnswer = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.id}"