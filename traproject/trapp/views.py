from django.http import HttpResponse
from django.shortcuts import render
from .models import Places, Team


# Create your views here.
def demo(request):
    obj=Places.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
