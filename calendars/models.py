from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

User = get_user_model()

# Create your models here.
class Availability(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
