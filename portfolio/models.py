from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=30)
    key = models.CharField(max_length=30, primary_key=True)
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.key
        
    def __unicode__(self):
        return self.key

class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    detail = models.TextField()
    client = models.CharField(max_length = 20)
    image = models.FileField(upload_to='images/project')
    requirements = models.TextField()
    domain = models.CharField(max_length = 20)
    website = models.URLField()
    categories = models.ManyToManyField(Category)