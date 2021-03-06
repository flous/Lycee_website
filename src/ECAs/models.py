from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.urls import reverse
import os
from django.conf import settings
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
    act_date = models.DateTimeField(default=timezone.now)
    act_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE , related_name='author')
    type = models.ForeignKey(TypeActivities,on_delete=models.CASCADE , related_name='activities' , verbose_name='نوع النشاط ')
    class Meta:
        ordering=('-act_date',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('act_detail', args=[self.id])
class ImagesActivities(models.Model):
    image =models.ImageField(default='default/defaultActivitiesImage.jpg', upload_to='ActivitiesImages')
    activitie = models.ForeignKey(Activities , on_delete=models.CASCADE,related_name='images')
    def __str__(self):
        return self.image.url
    def save(self , *args , **kwarg):
        super().save(*args , **kwarg)
        img = Image.open(self.image.path)
        if ((img.width > 500) or (img.height > 500)):
            output_size = (500 , 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
