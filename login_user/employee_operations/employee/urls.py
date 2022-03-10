from django.urls import path
from employee import views
from .views import LoginView, LogoutView, RegisterView, findView, UserView, getemployee,deleteemployee,updateemployee

urlpatterns = [
    # employee urls
    path('get', getemployee),
    path('find/<str:uname>', findView),
    path('add',views.addemployee),
    path('delete/<str:uname>', deleteemployee),
    path('update', updateemployee),
    
    # user authentication url
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view(), name='login'),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
]