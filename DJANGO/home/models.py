from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    title=models.CharField(max_length=200)
    para=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,models.CASCADE,related_name='notes')
