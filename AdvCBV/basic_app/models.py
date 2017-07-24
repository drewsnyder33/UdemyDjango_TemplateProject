from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    # the following method makes it so that whenever someone hits 'submit' on create page to
    # create a new school, they are taken to the newly created school's detail page 
    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students') # related_name allows us to call this parameter later by name

    def __str__(self):
        return self.name
