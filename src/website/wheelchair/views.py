from rest_framework import generics

from wheelchair.models import Task
from wheelchair.forms import SignUpForm, TaskForm
from .serializers import TaskSerializer
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
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

class TaskView(CreateView):
    form_class = TaskForm
    template_name = "wheelchair/task_create.html"
    success_url = reverse_lazy("index")

    def form_valid(self,form):
        data = form.save(commit=False)
        data.user = self.request.user
        data.save()
        return super().form_valid(form)

def index(request):
    task_list = Task.objects.order_by('time')[:10]
    context={'task_list' : task_list}
    return render(request, 'wheelchair/index.html', context)
