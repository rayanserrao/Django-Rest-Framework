from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerialzer
from rest_framework import status
from rest_framework import viewsets

# Create your views here.

class StudnetViewSets(viewsets.ViewSet):
    def list(self,request):
        stu = Student.objects.all()
        serilaizer = StudentSerialzer(stu,many=True)
        return Response(serilaizer.data)
    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id= id)
            serializer = StudentSerialzer(stu)
            return Response(serializer.data)
    def create(self,request):
        serializer = StudentSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def update(self,request,pk=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerialzer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerialzer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data partialy updated'},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request,pk=None):
        id = pk
        stu = Student.objects.get(id=pk)
        stu.delete()
        return Response({'msg':'data deleted'})

