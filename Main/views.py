from rest_framework.views import APIView
from .models import *
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
# Create your views here.
from .serializers import *
import jwt, datetime


class LoginView(APIView):

    def get(self, request):
        return Response({
            'message' : 'success'
        })
        
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('user not found')

        checkpass = User.objects.filter(password= password).first()
        if checkpass is None:
            raise AuthenticationFailed('wrong password')
        
        payload = {
            'id' : user.id,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat' : datetime.datetime.utcnow()
        }   
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        res = Response()
        res.set_cookie(key='jwt', value = token , httponly = True)
        res.data = {
            'jwt' :  token,
        }
        
        return res

class userView(APIView):
    def get(self, request):
        cookie = request.COOKIES.get('jwt')
        
        if not cookie:
            raise AuthenticationFailed('user not found')
        try:
            payload = jwt.decode(cookie, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user = User.objects.filter(id=payload['id']).first()
        serializers = UserSerializer(user)
        
        return Response(serializers.data)
        