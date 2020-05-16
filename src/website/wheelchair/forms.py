from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('station', 'door', 'car', )
