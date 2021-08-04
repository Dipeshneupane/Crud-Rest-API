from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    isbn = models.CharField(max_length = 100)
    publisher = models.CharField(max_length = 100)

    def __str__(self):
        return self.title
    
