from django.shortcuts import render

# Create your views here.
from .models import delaytime
from django.http import HttpResponse


def index(request):
    sec=delaytime.objects.all()
    template='button/index.html'
    context={
            'sec':sec,
            }
    if request.method == 'POST':
        if 'button_1' in request.POST:
            delaytime.objects.all().delete()
            t=delaytime(delaysec=100)
            t.save()
        elif 'button_2' in request.POST:
            delaytime.objects.all().delete()
            t=delaytime(delaysec=500)
            t.save()
    return render(request,template,context)

def data(request):
    sec=delaytime.objects.get().delaysec
    return HttpResponse(sec)
