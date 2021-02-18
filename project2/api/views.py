from django.shortcuts import render
from .serialzers import StudentSerialzer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def StudentCreate(request):
    if request.method == 'POST':
        json_data = request.body  # geting json data
        stream = io.BytesIO(json_data)  # converting stream
        python_data = JSONParser().parse(stream)  # python data
        serializer = StudentSerialzer(data = python_data)  # complex data

        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
