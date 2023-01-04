from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from . import models
from rest_framework.authtoken.models import Token
from .serializers import (
    ApplicantSerializer,
    ReviewsSerializer
)
import datetime
# Create your views here.    

class ApplicantListApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        applicants = models.Applicant.objects.all()
        for a in applicants:
            a.register_time=datetime.datetime.strftime(a.register_time, "%Y-%m-%d %H:%M:%S")
        serializer = ApplicantSerializer(applicants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = ApplicantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ApplicantDetailApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return models.Applicant.objects.get(id=id)
        except models.Applicant.DoesNotExist:
            return None

    def get(self, request, applicant_id,*args, **kwargs):
        applicant = self.get_object(applicant_id)
        if not applicant:
            return Response(
                {"res": "Object with id " + str(applicant_id) +" does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = ApplicantSerializer(applicant)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, applicant_id,*args, **kwargs):
        applicant = self.get_object(applicant_id)
        if not applicant:
            return Response(
                {"res": "Object with id " + str(applicant_id) +" does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = JSONParser().parse(request)
        serializer = ApplicantSerializer(instance=applicant, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, applicant_id,*args, **kwargs):
        applicant = self.get_object(applicant_id)
        if not applicant:
            return Response(
                {"res": "Object with id " + str(applicant_id) +" does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        applicant.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
        
class ReviewsListApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        token = request.headers["Authorization"].split(" ")[1]
        usr = Token.objects.get(pk=token)
        reviews = models.Review.objects.filter(user = usr.user)
        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        token = request.headers["Authorization"].split(" ")[1]
        usr = Token.objects.get(pk=token)
        data = JSONParser().parse(request)
        data["user"] = usr.user.id
        serializer = ReviewsSerializer(data=data)
        if serializer.is_valid():
            aplc = models.Applicant.objects.get(id=serializer.data.get("applicant"))
            rv, _ = models.Review.objects.get_or_create(applicant=aplc, user=usr.user)
            rv.score = serializer.data.get("score")
            rv.save()
            divisor=0
            divident=0
            for review in models.Review.objects.filter(applicant=aplc):
                if review.score != 0:
                    divisor += review.score
                    divident += 1
            if divident == 0:
                aplc.avg_score = 0
            else:
                aplc.avg_score = divisor/divident
            aplc.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)