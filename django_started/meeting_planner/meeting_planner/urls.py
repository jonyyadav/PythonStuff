"""meeting_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from meeting import views
from meeting.views import detail, rooms_list
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenVerifyView,TokenRefreshView
from meeting.views import LoginAPI

from website.views import welcome
from meeting import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome,name="welcome"),
    path('rooms',rooms_list,name="rooms"),
    path('meetings/<int:id>', detail,name="detail"),
    path('meetings/new',views.new,name="new"),
    path('signup/',views.sign_up,name="signup"),
    path('login/',views.log_in,name="login"),
     path('api/token/',
         jwt_views.TokenObtainPairView.as_view(),
         name ='token_obtain_pair'),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name ='token_refresh'),
     path('hello/',views.TestAPI.as_view()) ,
     path('login_api',views.LoginAPI.as_view(),name="login_api")  , 
]
