from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=140, blank=False, null=False)
    description = RichTextField(null=True)
    featured_image = models.ImageField(blank=True, null=True)
    link = models.URLField(max_length=50, blank=False, null=True)
    category = models.CharField(max_length=140, blank=False, null=True)
    technology = models.CharField(max_length=140, blank=False, null=True)

    def __str__(self):
        return self.title


class Person(models.Model):
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    hero_text = RichTextField(null=True)

    facebook = models.URLField(max_length=50, blank=False, null=False)
    linkedin = models.URLField(max_length=50, blank=False, null=False)
    instagram = models.URLField(max_length=50, blank=False, null=False)
    youtube = models.URLField(max_length=50, blank=False, null=False)
    git = models.URLField(max_length=50, blank=False, null=False)
    behance = models.URLField(max_length=50, blank=False, null=False)

    about_me = RichTextField(null=True)

    address = models.CharField(max_length=40, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    email = models.CharField(max_length=25, blank=False, null=False)

    resume = models.FileField(upload_to='static/uploads/', blank=True, null=True)

    def __str__(self):
        return self.first_name


class Experience(models.Model):
    position = models.CharField(max_length=140, blank=False, null=False)
    company = models.CharField(max_length=140, blank=False, null=False)
    date_to = models.CharField(max_length=100, blank=False, null=False)
    date_from = models.CharField(max_length=100, blank=False, null=False)
    description = RichTextField(null=True)

    def __str__(self):
        return self.position


class Education(models.Model):
    degree = models.CharField(max_length=70, blank=False, null=True)
    institution = models.CharField(max_length=140, blank=False, null=False)
    date_to = models.CharField(max_length=100, blank=False, null=False)
    date_from = models.CharField(max_length=100, blank=False, null=False)
    # description = RichTextField(null=True)

    def __str__(self):
        return self.degree


class Skill(models.Model):
    technology = models.CharField(max_length=25, blank=False, null=True)
    progress = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.technology


class SkillD(models.Model):
    description = RichTextField(null=False)

    def __str__(self):
        return self.description


class Testimonial(models.Model):
    name = models.CharField(max_length=25, blank=False, null=True)
    position = models.CharField(max_length=140, blank=False, null=False)
    company = models.CharField(max_length=140, blank=False, null=False)
    headshot = models.ImageField(blank=True, null=True)
    feedback = RichTextField(null=True)

    def __str__(self):
        return self.name
