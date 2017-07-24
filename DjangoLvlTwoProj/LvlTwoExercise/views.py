from django.shortcuts import render
# from LvlTwoExercise.models import User
from LvlTwoExercise.forms import UserRegForm

# Create your views here.
def index(request):
    my_dict = {'index_tag': "Inserted from index view in views.py"}
    return render(request, 'LvlTwoExercise\index.html', context=my_dict)

def lvlTwo(request):
    my_dict = {'index_tag': "Inserted from lvlTwo view in views.py"}
    return render(request, 'LvlTwoExercise\index.html', context=my_dict)

# def users(request):
#     user_list = User.objects.order_by('last_name')
#     my_dict = {'user_results': user_list}
#     return render(request, 'LvlTwoExercise/users.html', context=my_dict)

def users(request):
    form = UserRegForm()

    if request.method == 'POST':
        form = UserRegForm(request.POST)

        if form.is_valid():
            # print("Validation success!")
            # print("Name: " + form.cleaned_data['name'])
            # print("Email: " + form.cleaned_data['email'])
            form.save(commit=True)
            # Take user back to home page:
            return index(request)
        else:
            print('ERROR: Form invalid.')

    return render(request,'LvlTwoExercise/users.html',{'form_tag':form})

    # user_list = User.objects.order_by('last_name')
    # my_dict = {'user_results': user_list}
    # return render(request, 'LvlTwoExercise/users.html', context=my_dict)
