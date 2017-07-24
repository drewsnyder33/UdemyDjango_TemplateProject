from django.conf.urls import url
from LvlTwoExercise import views

urlpatterns = [
    url(r'^$', views.users, name='users'),
]
