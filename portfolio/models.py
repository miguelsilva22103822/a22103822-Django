from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.name
