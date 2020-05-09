from django.db import models
from django.conf import settings
from personal_website.storage import OverwriteStorage
import os

# Create your models here.
def resume_path(instance, filename):
    return os.path.join(settings.STATIC_ROOT, 'Resume.pdf')
    
class Image(models.Model):
    Image = models.FileField(upload_to='images/')

class Resume(models.Model):
    Resume = models.FileField(max_length=50,storage=OverwriteStorage(), upload_to=resume_path)

    
