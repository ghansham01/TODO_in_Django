from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .models import Task

# Create your views here.
class login(LoginView):
    template_name= 'base/login.html'
    fields= '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class Tasklist(ListView):
    model = Task
    context_object_name = 'tasks' 
    template_name = 'base/task_list.html'  

class Taskdetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task_detail.html'


class TaskcreateView(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_form.html'

class TaskUpadateView(UpdateView):
    model= Task
    fields ='__all__'
    success_url = reverse_lazy('tasks')
    
class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_delete.html'
    
