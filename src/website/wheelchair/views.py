from rest_framework import generics

from wheelchair.models import Task
from wheelchair.forms import SignUpForm
from .serializers import TaskSerializer
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class TaskAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "wheelchair/signup.html" 
    success_url = reverse_lazy('api/')

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        login(self.request, user) # 認証
        self.object = user 
        return HttpResponseRedirect(self.get_success_url()) # リダイレクト
