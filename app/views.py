from django.shortcuts import render
from .serializers import *
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.

from rest_framework import viewsets
from rest_framework.views import APIView

class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request):
        serelize = CreateUserSerializer(data=request.data)
        serelize.is_valid(raise_exception=True)
        objectUser = serelize.validated_data
        token, _ = Token.objects.get_or_create(user=objectUser)
        return Response({"data": serelize.data, "token": token.key}, status=status.HTTP_201_CREATED, headers={"Access-Control-Allow-Origin": "*"})

class LoginUser(APIView):
    def post(self,request):
        serelize = LoginUserSerializer(data=request.data)
        serelize.is_valid(raise_exception=True)
        objectUser = serelize.validated_data
        token, _ = Token.objects.get_or_create(user=objectUser)
        return Response({"data": serelize.data, "token": token.key}, status=status.HTTP_200_OK, headers={"Access-Control-Allow-Origin": "*"})