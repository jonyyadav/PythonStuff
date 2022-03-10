from django.http import HttpResponse
from django.shortcuts import render

from meeting.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html",{"meetings":Meeting.objects.all()})


def hlo(request):
    return HttpResponse("Haan bhai kya haal")

# Create your views here.
