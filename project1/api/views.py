from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Create your views here.

# single object data
def StudentDetail(request,pk):
    # stu = Student.objects.get(id = 1)
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type = 'application/json')

    # two lines can be merged together and write as
    return JsonResponse(serializer.data)


# query set
def StudentALLDetail(request):
    # stu = Student.objects.get(id = 1)
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = 'application/json')
