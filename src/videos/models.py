from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Level(models.Model):
    level=models.CharField(max_length=100)
    def __str__(self):
        return self.level
class Branch (models.Model):
    branch=models.CharField(max_length=100)
    Level=models.ForeignKey(Level,on_delete=models.CASCADE , related_name='branches' , verbose_name='المستوى')
    def __str__(self):
        return '{} {}'.format(self.Level , self.branch)
class Module (models.Model):
    module        =models.CharField(max_length=100 , verbose_name='المستوى')
    coefficient   =models.PositiveSmallIntegerField(blank=True, null=True ,verbose_name='المعامل')
    hours_per_year=models.PositiveSmallIntegerField(blank=True, null=True , verbose_name='الحجم الساعي السنوي') 
    hours_per_week=models.PositiveSmallIntegerField(blank=True, null=True , verbose_name='الحجم الساعي الأسبوعي') 
    average_expression=models.CharField(max_length=100 , null=True, verbose_name='كيفية حساب المعدل')
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE , related_name='modules' , verbose_name='الشعبة')
    def __str__(self):
        return  '{} {}  '.format(self.module , self.branch)
class Video (models.Model):
    title=models.CharField(max_length=100 ,verbose_name='العنوان')
    description=models.TextField(blank=True, null=True , verbose_name='الوصف')
    link=models.CharField(max_length=300 , verbose_name='الرابط')
    module=models.ForeignKey(Module,on_delete=models.CASCADE , related_name='videos' , verbose_name='خاص بمادة ')
    vedio_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
            return self.title
    class Meta:
        ordering=('-vedio_date',)
    def get_absolute_url(self):
        return reverse('videos', args=[self.module.id])