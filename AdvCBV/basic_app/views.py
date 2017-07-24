from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                CreateView,UpdateView,DeleteView)
# from django.http import HttpResponse
from . import models

# Create your views here.
# # Below is function-based view for home page
# def index(request):
#     return render(request, 'index.html')

# # class-based view
# class CBView(View):
#     def get(self,request):
#         return HttpResponse("CLASS BASED VIEWS ARE COOL!")

# class-based view for home page
class IndexView(TemplateView):
    template_name = 'index.html'
    # note that it's looking in template directory listed in settings, so
    # if you bury this HTML file within another folder like "basic_app",
    # you'd have to put 'basic_app/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic Injection!'
        return context

class SchoolListView(ListView):
    model = models.School
    # ListView object that we inherit from automatically makes a context dictionary named as model name
    # ("School" in this case), puts it in lower case, and appends "_list"
    # which is a context dictionary including all the entries for this model.
    # Thus, in 'school_list.html', we can reference this "school_list" dictionary to loop through all records.
    # Note that if we'd like, we can set that list context dictionary name with a line as follows:
    # context_object_name = 'desiredName'

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'
    # similar to above, DetailView object that we inherit from automatically makes a context dictionary,
    # named as the model in lower case ("school" in this case). We could override
    # this default context dictionary naming with a line like the following:
    # context_object_name = 'desiredName'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list") # telling it which page to show after successfully deleting a school
