from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import *
# from .forms import ModeForm
# Create your views here.
def index(request):
    obj=place.objects.all()
    b=tourdate.objects.all()
    return  render(request,'index.html',{'r':obj,'s':b})

