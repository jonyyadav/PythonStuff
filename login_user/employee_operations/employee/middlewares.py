
from rest_framework.exceptions import AuthenticationFailed
import jwt

def login_middleware(get_response):
    def middleware(request):
        if request.path.endswith('/login'):
            pass
           
        else:
            token = request.COOKIES.get('jwt')
            if not token:
                raise AuthenticationFailed('Unauthenticated')

        
            try:
                jwt.decode(token, 'secret', algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                raise AuthenticationFailed('Unauthenticated')

            
        response = get_response(request)
        return response

    return middleware


