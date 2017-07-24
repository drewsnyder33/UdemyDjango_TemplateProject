from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'insert_tag': "Home Page"}
    return render(request, 'AppTwo/index.html', context=my_dict)

def help(request):
    my_dict = {'insert_tag': "Help Page"}
    return render(request, 'AppTwo/index.html', context=my_dict)

def pic(request):
    my_dict = {}
    return render(request, 'AppTwo/pic.html', context=my_dict)
