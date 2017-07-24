from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    url(r'^$', views.help, name='help'),
    url(r'^pic/', views.pic, name='pic')
]
