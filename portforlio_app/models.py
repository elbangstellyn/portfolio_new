from django.db import models

# Create your models here.

class PortforlioDetail(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(blank=False,null=False)
    image = models.ImageField(upload_to='port_image/')

    def __str__(self):
        return self.title
    

class Projects(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.CharField(max_length=300, blank=True, null=True)
    date =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    name = models.CharField(max_length=150)
    comment = models.TextField()
    project_commented = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Stack(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='stack/')

    def __str__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='framework/') 

    def __str__(self):
        return self.name
    
class Cv(models.Model):
    name = models.CharField(max_length=150)
    cv = models.FileField(upload_to='documents/')
    def __str__(self):
        return self.name
    
class About(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='about/')
    body = models.TextField()

    def __str__(self):
        return self.title
