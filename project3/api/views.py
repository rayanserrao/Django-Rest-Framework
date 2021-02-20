from django.shortcuts import render
from .models import Student
from .serialzers import StudentSerailzer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id  = python_data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serialzer = StudentSerailzer(stu)
            json_data = JSONRenderer().render(serialzer.data)
            return HttpResponse(json_data,content_type = 'application/json')
        stu = Student.objects.all()
        serializer = StudentSerailzer(stu,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type = 'application/json')

    if request.method == 'POST':
        json_data= request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerailzer(data = python_data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data craeted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')

        json_data = JSONRenderer().render(serializer.errors)  # predefined errors
        return HttpResponse(json_data,content_type = 'application/json')
    if request.method == 'PUT':
        json_data= request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerailzer(stu,data = python_data, partial =True)
        if serializer.is_valid():

            serializer.save()
            res = {'msg':'data updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')

        json_data = JSONRenderer().render(serializer.errors)  
        return HttpResponse(json_data,content_type = 'application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu  = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'data deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type = 'application/json')


        

