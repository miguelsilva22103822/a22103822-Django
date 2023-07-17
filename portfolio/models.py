from django.db import models


class Author(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=callable)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    text = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)
    post_id = models.ForeignKey(Post, on_delete=callable)

    def __str__(self):
        return self.text


class Contact(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='icons/', null=True, blank=True)
    link_url = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    is_url_link = models.BooleanField()

    def __str__(self):
        return self.name


class Year(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return f'{self.number}'


class Semester(models.Model):
    year = models.ForeignKey(Year, on_delete=callable)
    number = models.IntegerField()

    def __str__(self):
        return f'Year {self.year}, Semester {self.number}'


class Subject(models.Model):
    semester = models.ForeignKey(Semester, on_delete=callable)
    name = models.CharField(max_length=100)
    nr_credits = models.IntegerField()
    ranking = models.IntegerField()

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    linked_in_url = models.CharField(max_length=100)
    moodle_url = models.CharField(max_length=100)
    subject_teaching = models.ManyToManyField(Subject, related_name='person_set')

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    link = models.CharField(max_length=200)
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)

    def __str__(self):
        return self.title
