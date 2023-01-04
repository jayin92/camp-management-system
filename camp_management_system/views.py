from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token

class UserDetailApiView(APIView):
    def post(self, request):
        token = request.headers["Authorization"].split(" ")[1]
        usr = Token.objects.get(pk=token)

        if not usr:
             return Response(
                {"res": "Object with token " + str(token) +" does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = {
            "username": str(usr.user)
        }
        return Response(data, status=status.HTTP_200_OK)
        

class Logout(APIView):
    def post(self, request, *args, **kwargs):
        token = request.headers["Authorization"].split(" ")[1]
        usr = Token.objects.get(pk=token)
        if not usr:
             return Response(
                {"res": "Object with token " + str(token) +" does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        usr.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )