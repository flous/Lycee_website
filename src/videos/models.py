from django.db import models

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
    module        =models.CharField(max_length=100)
    coefficient   =models.PositiveSmallIntegerField(blank=True, null=True)
    hours_per_year=models.PositiveSmallIntegerField(blank=True, null=True) 
    hours_per_week=models.PositiveSmallIntegerField(blank=True, null=True) 
    average_expression=models.CharField(max_length=100 , null=True)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE , related_name='modules' , verbose_name='الشعبة')
    def __str__(self):
        return self.module
class Video (models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True, null=True)
    link=models.CharField(max_length=128)
    module=models.ForeignKey(Module,on_delete=models.CASCADE , related_name='videos' , verbose_name='المادة')
    def __str__(self):
            return self.title