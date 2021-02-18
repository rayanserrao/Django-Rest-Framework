from rest_framework import serializers
from .models import Student

class StudentSerialzer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=30)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)