from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404


from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


def getUsername(request: Request) -> str:
    return request.data['username']

def getPassword(request: Request) -> str:
    return request.data['password']

def notFound():
    return status.HTTP_400_BAD_REQUEST



@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def login(request):

    if request.method == 'GET':
        return Response({"message": "Needs No Auth"})

    user = get_object_or_404(User, username=getUsername(request))
    if not user.check_password(getPassword(request)):
        return Response({'detail': 'Not Found'}, status=notFound())
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def signup(request):

    if request.method == 'GET':
        return Response({"message": "Needs No Auth"})

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"user": dict(user), "token": token.key})
    return Response(serializer.errors, status=notFound())


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    
    just_username = User(request).get_username()
    return Response({"message": "Passed!", "user": str(request.user), "just_username": just_username})