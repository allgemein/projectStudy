from django.shortcuts import render,redirect

# Create your views here.
from .models import status
from django.http import HttpResponse


def index(request):
    template='button/index.html'
    if request.method == 'POST':
        tmp=status.objects.last()
        if(50<status.objects.count()):
            status.objects.all().delete()
            tmp.save()
        if 'button_1' in request.POST:
            t=status(direction=("back" if tmp.direction=="front" else "front"),power=1)
            t.save()
        elif 'button_2' in request.POST:
            t=status(direction=tmp.direction,power=(0 if tmp.power else 1))
            t.save()
        return redirect("./")
    context = {
            'status' : status.objects.last()
            }
    return render(request,template,context)

def data(request):
    res=(status.objects.last().direction)
    if(status.objects.last().power):
        res="stop"
    return HttpResponse(res)
