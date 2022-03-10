from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import make_password
import jwt
import datetime


from .models import Employee, User
from .serializers import EmployeeSerializer, UserSerializer


   
def logout(request):
        response=Response()
        response.delete_cookie('JWToken')
        response.data={
            'message':'logout success'
        }
        return response

def getuser( request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        u_serializer = UserSerializer(user)
        return Response(u_serializer.data)   

def login(request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=1),
            'iat': datetime.datetime.now()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response() 
        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt': token
        }

        return response        

def register(request):
        u_serializer = UserSerializer(data=request.data)
        u_serializer.is_valid(raise_exception=True)
        u_serializer.save()
        return Response(u_serializer.data)   

def delete(request,uname):
     if request.method == 'DELETE':
        employee = Employee.objects.get(username=uname)
        employee.delete()
        return JsonResponse("Deleted successfully", safe=False)


def add(request):
    if request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_data["password"] = make_password(employee_data["password"])
        e_serializer = EmployeeSerializer(data=employee_data)
        if e_serializer.is_valid():
            e_serializer.save()
            return JsonResponse("Added successfully", safe=False)

        else:
            return JsonResponse("Failed to add", safe=False)  

def get(request):
     if request.method == 'GET':
        employee = Employee.objects.all()
        e_serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(e_serializer.data, safe=False)

def find(request,uname):
    if request.method == 'GET':
        employee = Employee.objects.get(username=uname)
        e_serializer = EmployeeSerializer(employee)
        return JsonResponse(e_serializer.data, safe=False)    

def update(request):
     if request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee_data["password"] = make_password(employee_data["password"])
        employee = Employee.objects.get(username=employee_data['username'])
        print(employee)
        e_serializer = EmployeeSerializer(employee, data=employee_data)
        if e_serializer.is_valid():
            e_serializer.save()
            return JsonResponse("Updated successfully", safe=False)

        else:
            return JsonResponse("Failed to update", safe=False)             