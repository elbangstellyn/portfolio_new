from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.


class PortforlioDetail(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    image = CloudinaryField('image')

class Projects(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    image = CloudinaryField('image')
    link = models.CharField(max_length=300, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

class Stack(models.Model):
    name = models.CharField(max_length=150)
    image = CloudinaryField('image')

class Framework(models.Model):
    name = models.CharField(max_length=150)
    image = CloudinaryField('image')

class About(models.Model):
    title = models.CharField(max_length=150)
    image = CloudinaryField('image')
    body = models.TextField()

class Cv(models.Model):
    name = models.CharField(max_length=150)
    cv = CloudinaryField('raw')


    
class Comment(models.Model):
    name = models.CharField(max_length=150)
    comment = models.TextField()
    project_commented = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name