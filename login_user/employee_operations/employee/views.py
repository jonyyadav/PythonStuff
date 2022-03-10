from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from employee.service import logout, getuser, login, register, add, delete, get, find, update

# end points get all, update, find, delete


@csrf_exempt
def getemployee(request):
    response = get(request)
    return response


@csrf_exempt
def updateemployee(request):
    response = update(request)
    return response


@csrf_exempt
def deleteemployee(request, uname):
    response = delete(request, uname)
    return response


@csrf_exempt
def addemployee(request):
    response = add(request)
    return response


def findView(request, uname):
    response = find(request, uname)
    return response


# user registration
class RegisterView(APIView):
    def post(self, request):
        response = register(request)
        return response

# user login


class LoginView(APIView):
    def post(self, request):
        response = login(request)
        return response

# user view


class UserView(APIView):
    def get(self, request):
        response = getuser(request)
        return response

# user logout


class LogoutView(APIView):
    def post(self, request):
        response = logout(request)
        return response
