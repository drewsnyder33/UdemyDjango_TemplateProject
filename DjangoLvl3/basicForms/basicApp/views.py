from django.shortcuts import render
from basicApp import forms

# Create your views here.
def index(request):
    return render(request,'basicApp/index.html')

def form_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation success!")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])

    return render(request,'basicApp/form_page.html',{'form_tag':form})
