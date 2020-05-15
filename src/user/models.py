from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    image =models.ImageField(default='default.png', upload_to='profile_pics')
    user = models.OneToOneField(User , on_delete=models.CASCADE)
