from django.shortcuts import render
import datetime as dt
from .models import Image

def welcome(request):
    photo = Image.photo_details()
    return render(request,'home.html',{"photo":photo})
