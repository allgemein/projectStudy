from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task/new/',views.TaskView.as_view(),name='task_create'),
    path('api/', views.TaskAPIView.as_view(),name='api'),
    path('accounts/signin/',views.signin,name='signin'),
    path('accounts/signup/',views.SignUp.as_view(),name='signup'),
    path('accounts/signout/', views.signout, name='signout'),
    path('user/', views.userpage, name='userpage')
]
