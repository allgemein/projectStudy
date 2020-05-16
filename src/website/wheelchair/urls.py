from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.TaskAPIView.as_view()),
    path('accounts/signup/',views.SignUp.as_view(),name='signup')
]
