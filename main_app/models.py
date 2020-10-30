from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

USES = (
    ('I', 'Inspo'),
    ('W', 'Writing')
)

# Create your models here.
class Photo(models.Model):
    url = models.CharField(max_length=100)
    photographer = models.CharField(max_length=100)
    photographer_url = models.CharField(max_length=100)
    src_medium = models.CharField(max_length=100)

    def __str__(self):
        return self.url


class Album(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    created = models.DateField(auto_now_add=True)
    use = models.CharField(
        max_length=1,
        choices=USES,
        default=USES[0][0]
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photos = models.ManyToManyField(Photo)
    
    def __str__(self):
        return self.name

