from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# @api_view()
# def hello_world(request):
#     return Response({'msg':'hello world'})  # primitive data type only 

# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg':'hello wolrd'})

@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg':'hello world'}) 

    if request.method == 'POST':
        print(request.data)
        
        return Response({'msg':'this is post request','data':request.data})

