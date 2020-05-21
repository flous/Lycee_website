from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
# Create your models here.
class TypeActivities(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default='default/defaultActivitiesImage.jpg', upload_to='TypeActivitiesImages')
    def __str__(self):
        return self.title
    def save(self , *args , **kwarg):
        super().save(*args , **kwarg)
        img = Image.open(self.image.path)
        if ((img.width > 300) or (img.height > 300)):
            output_size = (300 , 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
class Activities(models.Model):
    title = models.CharField(max_length=100)
    content  = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.ForeignKey(TypeActivities,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class ImagesActivities(models.Model):
    image =models.ImageField(default='default/defaultActivitiesImage.jpg', upload_to='ActivitiesImages')
    user = models.ForeignKey(Activities , on_delete=models.CASCADE)
