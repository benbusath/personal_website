from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=30)
    
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length = 100)
    desription = models.TextField()
    detail = models.TextField()
    image = models.FileField(path='/images')
    requirements = model.TextField()
    domain = models.CharField(max length = 20)
    website = models.URLField()
    categories = models.ManyToManyField(Category)