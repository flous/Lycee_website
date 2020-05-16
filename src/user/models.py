from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image
# Create your models here.
class Profile(models.Model):
    image =models.ImageField(default='default.jpg', upload_to='profile_pics')
    user = models.OneToOneField(User , on_delete=models.CASCADE)

    def __str__(self):
        return '{} profile . '.format(self.user.username)

    def save(self , *args , **kwarg):
        super().save(*args , **kwarg)
        img = Image.open(self.image.path)
        if ((img.width > 300) or (img.height > 300)):
            output_size = (300 , 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


def Create_profile(sender ,**kwarg):
    if  kwarg['created']:
        Profile.objects.create(user=kwarg['instance'])
post_save.connect(Create_profile , sender=User)