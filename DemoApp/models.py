from django.db import models

# Create your models here.

class signr(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=15)
    email = models.EmailField(primary_key=True)
    country = models.TextField()
    gender = models.CharField(max_length=10)
    language=models.CharField(max_length=50)

class publdata(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=10)
    movie_type = models.CharField(max_length=50)
    actors = models.TextField()
    plot = models.TextField()
    poster = models.URLField()
    email = models.EmailField(default="/")

class playdata1(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=10)
    movie_type = models.CharField(max_length=50)
    actors = models.TextField()
    plot = models.TextField()
    poster = models.URLField()
    email = models.EmailField(default="/")

class playdata2(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=10)
    movie_type = models.CharField(max_length=50)
    actors = models.TextField()
    plot = models.TextField()
    poster = models.URLField()
    email = models.EmailField(default="/")

class playdata3(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=10)
    movie_type = models.CharField(max_length=50)
    actors = models.TextField()
    plot = models.TextField()
    poster = models.URLField()
    email = models.EmailField(default="/")




