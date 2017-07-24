# from django.db import models
from django import forms
from LvlTwoExercise.models import User

# # Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length=64)
#     last_name = models.CharField(max_length=64)
#     email = models.EmailField(unique=True)

class UserRegForm(forms.ModelForm):
    # Could put custom validators here
    class Meta:
        model = User
        fields = "__all__"
