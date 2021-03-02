from django.db import models
from django.utils import timezone

# Create your models here.

class Feedback(models.Model):
    feedback = models.CharField(max_length=200)
    name = models.CharField(max_length=200,null=True,blank=True)
    created_date = models.DateTimeField(
        default=timezone.now, null=True, blank=True)
