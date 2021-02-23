from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serialzers import StudentSerailzer

# Create your views here.
@api_view(['GET','POST','PUT','DELETE'])
def student_data(request):
    if request.method == "GET":
        id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerailzer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerailzer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerailzer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'})
        return Response(serializer.errors)
    if request.method == 'PUT': 
        id = request.data.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerailzer(stu, data = request.data, partial=True)
        if serializer.is_valid():

            serializer.save()
            return Response({'msg':'data Updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data deleted'})
            

