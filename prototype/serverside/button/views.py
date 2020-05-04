from django.shortcuts import render

# Create your views here.
from .models import status
from django.http import HttpResponse


def index(request):
    template='button/index.html'
    if request.method == 'POST':
        if 'button_1' in request.POST:
            status.objects.all().delete()
            t=status(place=1)
            t.save()
        elif 'button_2' in request.POST:
            status.objects.all().delete()
            t=status(place=2)
            t.save()
        elif 'button_3' in request.POST:
            status.objects.all().delete()
            t=status(place=3)
            t.save()

    return render(request,template)

def data(request):
    res=status.objects.get().place
    return HttpResponse(res)
