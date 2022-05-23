from django.db import models
from django import forms
from matplotlib.widgets import Widget

# Create your models here.
class Coursechoices(models.Model):
    COURSE_CHOICES=(
        ('ICS', 'Introduction to Computer Systems'),
        ('IDS','Introduction to Data Science'),
        ('CSPP','Computer Science Principles and Programming')
    )
    name= models.CharField(max_length=25,choices=COURSE_CHOICES,unique=True)

    def __str__(self):
        return self.name

class  StudentData(models.Model):
    sname = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField()
    bio = models.TextField()
    coursesEnrolled =forms.ModelMultipleChoiceField(queryset=Coursechoices.objects,widget=forms.CheckboxSelectMultiple(),required=False)

    def __str__(self):
        return self.sname