from django.db import models

# Create your models here.
class   UserExams(models.Model):
    user_name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    examcode = models.IntegerField(unique=True)
    answers = models.TextField()
    score = models.FloatField()

    def __str__(self):
        return self.user_name
