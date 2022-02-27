from distutils.command.upload import upload
from django.db import models
from froala_editor.fields import FroalaField
# Create your models here.
from django.contrib.auth.models import User
from .hh import generate_slug
class BlogModel(models.Model):
    title=models.CharField(max_length=1000)
    content=FroalaField()
    slug=models.SlugField(max_length=1000, null=True, blank=True)
    image=models.ImageField(upload_to="blog")
    created_at=models.DateTimeField(auto_now_add=True)
    upload_to=models.DateTimeField(auto_now=True)
    author=models.CharField(max_length=1000,default="Uday Uppal")
    read_time=models.IntegerField(default=5)
    def __str__(self):
        return self.title
    def save(self, *args,**kwargs):
        self.slug=generate_slug(self.title)
        super(BlogModel,self).save(*args,**kwargs)
class contact_model(models.Model):
    email=models.EmailField()       
    subject=models.CharField(max_length=1000)
    message=FroalaField()
    def __str__(self):
        return self.email 
