from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serialzers import StudentSerailzer
from rest_framework import status

# Create your views here.


class StudentAPI(APIView):
    def get(self,request, pk=None, format = None):
        id = pk     # using web API
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerailzer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerailzer(stu, many=True)
        return Response(serializer.data)

    def post(self, request,format=None):
        serializer = StudentSerailzer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request, pk=None, format=None):
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerailzer(stu, data = request.data)
        if serializer.is_valid():

            serializer.save()
            return Response({'msg':'data complete Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerailzer(stu, data = request.data, partial=True)
        if serializer.is_valid():

            serializer.save()
            return Response({'msg':'data partialy Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data deleted'})


      



    
            

