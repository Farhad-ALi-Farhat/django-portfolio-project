from django.db import models

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    year_completed = models.IntegerField()

class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completion_date = models.DateField()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()



     
    