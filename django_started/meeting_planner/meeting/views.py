
import logging
from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
from rest_framework import status
from .models import Meeting, Room
from django.forms import modelform_factory
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
  
  



# Create your views here.
def detail(request, id):
    
      meeting = get_object_or_404(Meeting, pk=id)
      return render(request, "meeting/detail.html", {"meeting": meeting})
   



def rooms_list(request):
     return render(request, "meetings/rooms_detail.html", {"rooms": Room.objects.all()})
       
  


MeetingForm = modelform_factory(Meeting, exclude=[])


def new(request):
    if request.method=="POST":
        form=MeetingForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect("welcome")

    else:
        form = MeetingForm()
    return render(request, "meeting/new.html", {"form": form})


def sign_up(request):
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'account created')
            fm.save()
    else:
        fm=SignUpForm()
    return render(request,'meeting/signup.html',{'form':fm})    


def log_in(request):
    if request.method=="POST":
     fm=AuthenticationForm(request=request,data=request.POST)
     if fm.is_valid():
      uname=fm.cleaned_data['username']
      upass=fm.cleaned_data['password']
      user=authenticate(username=uname,password=upass)
      if user is not None:
          login(request,user)

          return HttpResponse("login success")
    else:
        fm=AuthenticationForm()
    return render(request,'meeting/login.html',{'form':fm})


class TestAPI(APIView):
    permission_classes = (IsAuthenticated, )
  
    def get(self,content):
       
         content = {'message': 'Hello'}
         return Response(content,status=status.HTTP_200_OK) 
         
       

class LoginAPI(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request, format = None):
        username = request.data['username'] 
        password = request.data['password'] 

        new_user = authenticate(username = username, password = password)
        if new_user is not None:
            url = 'http://localhost:8000/api/token/ username=qwerty password=0987uiop'
            # values = {
            #     'username' : 'qwerty',
            #     'password' : '0987uiop'
            # }
            r = request.post(url) 
            token_data = r.json() 
            return Response(token_data) 
        else:
            return Response({"status" : "Denied."}, status=status.HTTP_400_BAD_REQUEST)
