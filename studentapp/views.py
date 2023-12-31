from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from studentapp.forms import Studentsform
from studentapp.models import Students
from studentapp.serializer import Studentsserializer



@api_view(['GET','POST'])
def student_list(request):
    if request.method =='GET':
        student =Students.objects.all()
        serializer = Studentsserializer(student,many=True)
        return Response(serializer.data)
    elif request.method =="POST":
        serializer= Studentsserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)