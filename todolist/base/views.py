from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView,FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy

# import for Reordering feature
from django.views import View
from django.shortcuts import redirect
from django.db import transaction

from .models import Task
from .form import PostionFrom

# Create your views here.
class login(LoginView):
    template_name= 'base/login.html'
    fields= '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authentcted_user = True
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request)
        return super(RegisterPage,self).form_valid(form)
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        
        return super(RegisterPage, self).get(*args, **kwargs)
    

class Tasklist(ListView):
    model = Task
    context_object_name = 'tasks' 
    template_name = 'base/task_list.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context

class Taskdetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task_detail.html'


class TaskcreateView(CreateView):
    model = Task
    fields = ['title','description', 'complete']
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_form.html'


class TaskUpadateView(UpdateView):
    model= Task
    fields = ['title','description', 'complete']
    success_url = reverse_lazy('tasks')


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_delete.html'
    
class TaskReorder(View):
    def post(self,request):
        form = PostionFrom(request.POST)

        if form.is_valid():
            postionlist = form.cleaned_data["position"].split(',')

            with transaction.atomic():
                self.request.user.set_task_order(postionlist)

        return redirect(reverse_lazy('tasks'))