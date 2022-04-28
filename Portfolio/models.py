from django.db import models
from django.urls import reverse

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=255, blank=True)
    project_image = models.ImageField(upload_to='project', blank=True)

    def get_url(self):
        return reverse('project_details', args=[self.pk])

    def __str__(self):
        return self.title

class ProjectDetail(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField(max_length=400, blank=True)
    language = models.CharField(max_length=50)
    web_framework = models.CharField(max_length=50)
    front_end = models.CharField(max_length=100)
    website_link = models.URLField(blank=True)
    source_code = models.URLField(blank=True)

    def __str__(self):
        return self.project.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project', max_length=255)

    def __str__(self):
        return self.project.title

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.name