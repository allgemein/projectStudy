from rest_framework import generics

from wheelchair.models import Task
from wheelchair.forms import SignUpForm, TaskForm
from .serializers import TaskSerializer
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.shortcuts import render

class TaskAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "wheelchair/signup.html" 
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        login(self.request, user) # 認証
        self.object = user 
        return HttpResponseRedirect(self.get_success_url()) # リダイレクト

def signin(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'wheelchair/signin.html')
    except KeyError:
        return render(request, 'wheelchair/signin.html')

class TaskView(CreateView):
    form_class = TaskForm
    template_name = "wheelchair/task_create.html"
    success_url = reverse_lazy("index")

    def get(self, request, *args, **kwargs):
        try:
            user = self.request.user
            return super(TaskView, self).dispatch(request, *args, **kwargs)
        except:
            return HttpResponseRedirect(reverse('signin'))
    def form_valid(self,form):
        data = form.save(commit=False)
        data.user = self.request.user
        data.save()
        return super().form_valid(form)

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def index(request):
    return render(request, 'wheelchair/index.html')

def userpage(request):
    try:
        user=request.user
        task_list = Task.objects.filter(user=user)
        context={'task_list' : task_list}
        return render(request, 'wheelchair/userpage.html', context)
    except:
        return HttpResponseRedirect(reverse('signin'))
